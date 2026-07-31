---
title: "Esotrace viewer"
---

# Esotrace viewer

A GUI tool for viewing CTracer/EsoTrace binary log files from Audi MHS2 (MIB2 Evo High) head units.

EsoTrace is the logging framework used internally by the MHS2 system. It produces binary trace files containing structured log entries from various system processes. This viewer parses that binary format and presents the logs in a searchable, filterable table.

## **Features**

* Parses the EsoTrace binary packet format (big-endian, supports INIT, CREATE_ENTITY, LOG_DATA, and BULK_LOG_DATA message types)
* Load multiple trace files into a single session — entries are merged and sorted by timestamp
* Filter by log level (trace, debug, info, warn, error, fatal) and free-text search across channels and messages
* Color-coded log levels for quick visual scanning
* Detail pane showing full message content for the selected entry
* Export to plain text log or CSV (filtered or all entries)

## **Usage**

Run python esotrace_viewer.py to launch the GUI, or pass files directly:

```bash
python esotrace_viewer.py log_0000.esotrace log_0001.esotrace
```

No external dependencies — uses only Python standard library (tkinter).

## Download

[esotrace_viewer.py 30330](attachments/fdd33556-e8d7-4f59-8d8b-e2f42c32f4ed.py)