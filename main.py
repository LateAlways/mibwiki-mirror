import json
import os
import re
import time

import httpx
import shutil
from config import LAST_SIGNED_IN, ACCESS_TOKEN

BASE_URL = "https://mibwiki.one"
OUTPUT = "docs"

def safe_url_folder(url: str) -> str:
    return url.split("/", 2)[-1]

def sanitize_folder_name(name: str) -> str:
    final = re.sub(r'[<>:"/\\|?*]', ' ', name)
    # remove additional spaces at the end
    final = re.sub(r'\s+$', '', final)
    return final

def makeGET(endpoint) -> httpx.Response:
    return httpx.get(BASE_URL + endpoint, follow_redirects=True, cookies={
        "lastSignedIn": LAST_SIGNED_IN,
        "accessToken": ACCESS_TOKEN
    })

def makePOST(endpoint: str, data: dict=None, headers:dict=None) -> httpx.Response:
    return httpx.post(BASE_URL + endpoint, cookies={
        "lastSignedIn": LAST_SIGNED_IN,
        "accessToken": ACCESS_TOKEN,
    }, json=data, headers=headers)

def getCollections() -> list[dict]:
    collections = []
    endpoint = "/api/collections.list?limit=100&offset=0"
    while True:
        response = makePOST(endpoint)
        if response.status_code == 429:
            print("We are being ratelimited...")
            time.sleep(61)
            continue
        elif response.status_code != 200:
            print(f"Failed to get collections: Status code {str(response.status_code)}")
            return []
        else:
            collections_list = response.json()
            for collection in collections_list["data"]:
                collections.append(collection)

            if len(collections) >= collections_list["pagination"]["total"]:
                break
            else:
                endpoint = collections_list["pagination"]["nextPath"]

    return collections

def getCollectionDocuments(collectionId: str) -> list[dict]:
    while True:
        response = makePOST("/api/collections.documents", {"id": collectionId})
        if response.status_code == 429:
            print("We are being ratelimited...")
            time.sleep(61)
            continue
        elif response.status_code != 200:
            print(f"Failed to get documents for collection {collectionId}: Status code {str(response.status_code)}")
            return []

        documents_list = response.json()

        return documents_list["data"]

def getDocumentHTML(documentId: str) -> httpx.Response:
    return makePOST("/api/documents.export", {"id": documentId}, headers={"accept": "application/json, text/html"})

def getDocumentMarkdown(documentId: str) -> dict:
    return makePOST("/api/documents.export", {"id": documentId}).json()

def getDocumentsInfo(documentUrl: str) -> dict:
    while True:
        response = makePOST("/api/documents.info", {"apiVersion": 2, "id": safe_url_folder(documentUrl)})
        if response.status_code == 429:
            print("We are being ratelimited...")
            time.sleep(61)
            continue
        elif response.status_code != 200:
            print(f"Failed to get document info for {documentUrl}: Status code {str(response.status_code)}")
            return False
        else:
            return response.json()

def downloadAttachment(url: str) -> bytes:
    while True:
        response = makeGET(url)
        if response.status_code == 429:
            print("We are being ratelimited...")
            time.sleep(61)
            continue
        elif response.status_code == 200:
            return response.content, response.headers.get("content-disposition").split("filename=")[-1].strip('"').split(".")[-1]
        else:
            print(f"Failed to download attachment: Status code {str(response.status_code)}")
            return b"", "bin"

collections = {}

def recursiveSearchDocumentHelper(document: dict, docId: str) -> str | None:
    if safe_url_folder(document["url"]) == docId:
        return sanitize_folder_name(document["title"])
    for child in document["children"]:
        result = recursiveSearchDocumentHelper(child, docId)
        if result is not None:
            return f"{sanitize_folder_name(document['title'])}/{result}"
    return None

def recursiveSearchDocumentGetFullURL(docId: str) -> str | None:
    for id,collection in collections.items():
        for document in collection["documents"]:
            result = recursiveSearchDocumentHelper(document, docId)
            if result is not None:
                return f"/{sanitize_folder_name(collection['name'])}/{result}"
    return None

def downloadDocument(document: dict, startPath: str) -> dict:
    os.makedirs(os.path.join(startPath, sanitize_folder_name(document["title"])), exist_ok=True)
    with open(os.path.join(startPath, sanitize_folder_name(document["title"]), "title.txt"), "w", encoding="utf-8") as f:
        f.write(document["title"])
        f.close()

    with open(os.path.join(startPath, sanitize_folder_name(document["title"]), "url.txt"), "w", encoding="utf-8") as f:
        f.write(document["url"])
        f.close()

    with open(os.path.join(startPath, sanitize_folder_name(document["title"]), "id.txt"), "w", encoding="utf-8") as f:
        f.write(document["id"])
        f.close()

    with open(os.path.join(startPath, sanitize_folder_name(document["title"]), "index.md"), "w", encoding="utf-8") as f:
        while True:
            has_description = "description" in document.keys() and document["description"] is not None and document["description"] != ""
            if has_description:
                data = {
                    "data": document["description"],
                    "status": 200
                }
            else:
                data = getDocumentMarkdown(document["id"])
            if data["status"] == 429:
                print("We are being ratelimited...")
                time.sleep(61)
                continue
            elif data["status"] == 200:
                print("Download success.")
                original_content: str = data["data"]

                attachment_pattern = r"(/api/attachments\.redirect\?id=[a-z0-9\-]+)"
                matches = re.findall(attachment_pattern, original_content)
                for match in matches:
                    os.makedirs(os.path.join(startPath, sanitize_folder_name(document["title"]), "attachments"), exist_ok=True)
                    attachment_data, extension = downloadAttachment(match)
                    with open(os.path.join(startPath, sanitize_folder_name(document["title"]), "attachments", match.split('=')[1]+"."+extension), "wb") as af:
                        af.write(attachment_data)
                        af.close()
                    original_content = original_content.replace(match, f"attachments/{match.split('=')[1]}.{extension}")
                doc_pattern = r"(https://mibwiki\.one)?(/doc/[A-z0-9\-]+)"
                doc_matches = re.findall(doc_pattern, original_content)
                for doc_match in doc_matches:
                    document_path = recursiveSearchDocumentGetFullURL(safe_url_folder(doc_match[1]))
                    if document_path is not None:
                        print(document_path)
                        original_content = original_content.replace("".join(doc_match), f"{document_path}/")
                    else:
                        info = getDocumentsInfo(doc_match[1])
                        if not info:
                            continue
                        new_url = info["data"]["document"]["url"]
                        document_path = recursiveSearchDocumentGetFullURL(safe_url_folder(new_url))
                        if document_path is not None:
                            print(document_path)
                            original_content = original_content.replace("".join(doc_match), f"{document_path}/")
                        else:
                            print(f"Could not find document for link {doc_match[1]} in document {document['url']} ({document['title'] if 'title' in document.keys() else document['name']})")

                f.write(original_content)
                f.close()
                print("Success!")
            else:
                print(f"Failed to get document {document['url']} ({document["title"] if "title" in document.keys() else document["name"]}): Status code {str(data["status"])}")

            break

    for children in document["children"]:
        downloadDocument(children, startPath=os.path.join(startPath, sanitize_folder_name(document["title"])))

if __name__ == "__main__":
    os.makedirs(OUTPUT, exist_ok=True)
    for x in os.listdir(OUTPUT):
        if x != "index.md":
            shutil.rmtree(os.path.join(OUTPUT, x), ignore_errors=True)

    collections_l = getCollections()
    hierarchy = {}
    for collection in collections_l:
        collections[collection["id"]] = {
            "url": collection["url"],
            "name": collection["name"],
            "documents": getCollectionDocuments(collection["id"])
        }
        hierarchy[collection["name"]] = collections[collection["id"]]["documents"]


    with open(os.path.join(OUTPUT, "collections.json"), "w", encoding="utf-8") as f:
        json.dump(hierarchy, f, ensure_ascii=False, indent=4)
    for collection in collections_l:
        os.makedirs(os.path.join(OUTPUT, sanitize_folder_name(collection["name"])), exist_ok=True)

        document_format = {
            "title": collection["name"],
            "url": collection["url"],
            "id": collection["id"],
            "description": collection["description"],
            "children": getCollectionDocuments(collection["id"])
        }

        downloadDocument(document_format, OUTPUT)
