import io
import argparse
from ctypes import *
from pathlib import Path

u64 = c_ulonglong
u32 = c_uint
u16 = c_ushort
u8 = c_ubyte
char = c_char

SECTOR_SIZE = 2048

NVBOOT_CMAC_AES_HASH_LENGTH    = 4

def NVBOOT_BOOTDATA_VERSION(a, b):
    return ((((a) & 0xffff) << 16) | ((b) & 0xffff))

TEGRA_BOOTDATA_VERSION_T20 = NVBOOT_BOOTDATA_VERSION(0x2, 0x1)
TEGRA_BOOTDATA_VERSION_T30 = NVBOOT_BOOTDATA_VERSION(0x3, 0x1)


class tegra20_boot_info_table (Structure):
    _pack_ = 1
    _fields_ = [
        ("unused_data1", u32 * 14),
        ("bct_size", u32),
        ("bct_ptr", u32)
    ]


class tegra30_boot_config_table (Structure):
    _pack_ = 1
    _fields_ = [
        ("crypto_hash", u32 * NVBOOT_CMAC_AES_HASH_LENGTH),
        ("random_aes_blk", u32 * NVBOOT_CMAC_AES_HASH_LENGTH),
        ("boot_data_version", u32 ),
        ("unused_data1", u32 * 1016),
        ("unused_consumer_data1", u32 ),
        ("partition_table_logical_sector_address", u16 ),
        ("partition_table_num_logical_sectors", u16 ),
        ("unused_consumer_data", u32 * 502),
        ("unused_data", u32 * 3),
    ]

TEGRA_PT_MAGIC = 0xffffffff8f9e8d8b
TEGRA_PT_VERSION =     0x100
TEGRA_PT_AES_HASH_SIZE =     4
# TEGRA_PT_NAME_SIZE =     4
TEGRA_PT_NAME_SIZE =     24

TEGRA_PT_SDHCI_DEVICE_ID = 18
TEGRA_PT_SDHCI_DEVICE_INSTANCES = 4

TEGRA_PT_PART_TYPE_BCT =     1
TEGRA_PT_PART_TYPE_EBT =     2
TEGRA_PT_PART_TYPE_PT =     3
TEGRA_PT_PART_TYPE_GENERIC = 6
TEGRA_PT_PART_TYPE_GP1 =     9
TEGRA_PT_PART_TYPE_GPT =     10


class tegra_partition_mount_info (Structure):
    _pack_ = 1
    _fields_ = [
        ("device_id", u32 ),
        ("device_instance", u32 ),
        ("device_attr", u32 ),
        ("mount_path", u8 * TEGRA_PT_NAME_SIZE),
        ("file_system_type", u32 ),
        ("file_system_attr", u32 ),
    ]

class tegra_partition_info (Structure):
    _pack_ = 1
    _fields_ = [
        ("partition_attr", u32 ),
        ("__pad1", u32 ),
        ("logical_sector_address", u64 ),
        ("logical_sectors_num", u64 ),
        ("physical_sector_address", u64 ),
        ("physical_sectors_num", u64 ),
        ("partition_type", u32 ),
        ("__pad2", u32 ),
    ]

class tegra_partition (Structure):
    _pack_ = 1
    _fields_ = [
        ("partition_id", u32 ),
        ("partition_name", char * TEGRA_PT_NAME_SIZE),
        ("mount_info", tegra_partition_mount_info),
        ("part_info", tegra_partition_info),
    ]

class tegra_partition_header_insecure (Structure):
    _pack_ = 1
    _fields_ = [
        ("magic", u64 ),
        ("version", u32 ),
        ("length", u32 ),
        ("signature", u32 * TEGRA_PT_AES_HASH_SIZE),
    ]

class tegra_partition_header_secure (Structure):
    _pack_ = 1
    _fields_ = [
        ("random_data", u32 * TEGRA_PT_AES_HASH_SIZE),
        ("magic", u64 ),
        ("version", u32 ),
        ("length", u32 ),
        ("num_partitions", u32 ),
        ("__pad", u32 ),
    ]

class tegra_partition_table  (Structure):
    _pack_ = 1
    _fields_ = [
        ("insecure", tegra_partition_header_insecure),
        ("secure", tegra_partition_header_secure),
        ("partitions", tegra_partition * 15),
    ]

TEGRA_PT_HEADER_SIZE = (sizeof(tegra_partition_header_insecure) + 
    sizeof(tegra_partition_header_secure))


def tegra_partition_table_insec_hdr_valid(pt: tegra_partition):
    if pt.insecure.magic   != TEGRA_PT_MAGIC or \
        pt.insecure.version != TEGRA_PT_VERSION:
        print("insecure header: magic=0x%x ver=0x%x" %
                   (pt.insecure.magic,
                   pt.insecure.version))
        return 0
    return 1

def tegra_partition_table_sec_hdr_valid(pt: tegra_partition):
    pt_size = pt.secure.num_partitions

    pt_size *= sizeof(pt.partitions[0])
    pt_size += TEGRA_PT_HEADER_SIZE

    if (pt.secure.magic   != TEGRA_PT_MAGIC or \
        pt.secure.version != TEGRA_PT_VERSION or \
        pt.secure.length  != pt.insecure.length or \
        pt.secure.length  < pt_size):
        print("secure header: magic=0x%x ver=0x%x length=%u|%u|%u" % (
                   pt.secure.magic,
                   pt.secure.version,
                   pt.secure.length,
                   pt.insecure.length,
                   pt_size))
        return 0

    return 1

def tegra_partition_table_unencrypted(pt: tegra_partition):
    # AES IV, all zeros if unencrypted 
    if (pt.secure.random_data[0] or pt.secure.random_data[1] or \
        pt.secure.random_data[2] or pt.secure.random_data[3]) :
        print("encrypted partition table unsupported")
        return 0
    return 1

# def tegra_partition_type_valid(p: tegra_partition):
#     # const struct tegra_partition_type *ptype;
#     # unsigned int i

#     for (i = 0; i < ARRAY_SIZE(tegra_partition_expected_types); i++) {
#         ptype = &tegra_partition_expected_types[i];

#         if (ptype.name and not tegra_partition_name_match(p, ptype.name)):
#             continue

#         if (p.part_info.partition_type == ptype.type):
#             return 0

#         #  * Unsure about all possible types, let's emit error and
#         #  * allow to continue for now.
#         if not ptype.name:
#             return 1

#     return -1

# def tegra_partition_name_match(struct tegra_partition *p,
#                        const char *name)
# {
#     return !strncmp(p.partition_name, name, TEGRA_PT_NAME_SIZE)

def tegra_partition_valid(
                  p: tegra_partition,
                  prev: tegra_partition,
                  sector,
                  size):
    prev_pi: tegra_partition_info = prev.part_info
    sect_end = prev_pi.logical_sector_address + \
            prev_pi.logical_sectors_num
    # char *type, name[2][TEGRA_PT_NAME_SIZE + 1]
    # int err

    name_0 = p.partition_name
    name_1 = prev.partition_name

    # validate expected partition name/type */
    # err = tegra_partition_type_valid(ptp, p)
    # if (err):
    #     print("partition_type: [%s] partition_type=%u" % (
    #                name_0, p.part_info.partition_type))
    #     if err < 0:
    #         return false

    #     print("continuing, please update list of expected types")

    # validate partition table BCT addresses */
    if p.partition_name == "PT":
        if (sector != tegra_pt_logical_sector_address and
            size   != tegra_pt_logical_sectors_num):
            print("PT location: sector=%x size=%x" % (
                       sector, size))
            return False

        # if ptp.pt_entry_checked:
        #     print("(duplicated) PT\n")
        #     return False

        # ptp.pt_entry_checked = True

    if (sector + size < sector):
        print("size: [%s] integer overflow sector=%x size=%x" % (
                   name_0.decode(), sector, size))
        return False

    # validate allocation_policy=sequential (absolute unsupported) */
    # if (p != prev and sect_end > sector):
    #     print("allocation_policy: [%s] end=%x [%s] sector=%x size=%x" % (
    #                name_1, sect_end, name_0, sector, size))
    #     return False

    # if (ptp.dev_instance != p.mount_info.device_instance):
    #     print("device_instance: [%s] device_instance=%u|%u\n",
    #                name_0, ptp.dev_instance,
    #                p.mount_info.device_instance)
    #     return False

    # if (ptp.dev_id != p.mount_info.device_id):
    #     print("device_id: [%s] device_id=%u|%u\n",
    #                name_0, ptp.dev_id,
    #                p.mount_info.device_id)
    #     return false
    # }

    if (p.partition_id > 127):
        print("partition_id: [%s] partition_id=%u" % (
                   name_0, p.partition_id))
        return False

    # sect_end = 0 # TODO get_capacity(ptp.state.bdev.bd_disk)

    # /* eMMC boot partitions are below ptp.boot_offset */
    # if (sector < ptp.boot_offset):
    #     sect_end += ptp.boot_offset
    #     type = "boot"
    # } else:
    #     sector -= ptp.boot_offset
    #     type = "main"
    # }

    # /* validate size */
    # if (!size || sector + size > sect_end):
    #     print("size: [%s] %s partition boot_offt=%d end=%x sector=%x size=%x\n",
    #                name_0, type, ptp.boot_offset, sect_end,
    #                sector, size)
    #     return false
    # }

    print("| %s | start: 0x%08x | size: 0x%04x |" % (
            name_0.decode(), sector*SECTOR_SIZE, size*SECTOR_SIZE))

    return (name_0.decode(), p.partition_id, sect_end, sector, size)

parser = argparse.ArgumentParser(description='mmx backup parser')
parser.add_argument('backup', help='path to mmx backup file')

args = parser.parse_args()
print("Parsing", args.backup)

buffer = memoryview(Path(args.backup).read_bytes())
reader = io.BytesIO(buffer)

t30_bct = tegra30_boot_config_table()
reader.readinto(t30_bct)

if t30_bct.boot_data_version != TEGRA_BOOTDATA_VERSION_T30:
    raise SystemExit("Wrong boot_data_version: %s" % t30_bct.boot_data_version)

tegra_pt_logical_sector_address = t30_bct.partition_table_logical_sector_address
tegra_pt_logical_sectors_num = t30_bct.partition_table_num_logical_sectors

print("BCT found in Backup")
print("initialized to logical sector = %x sectors_num = %x\n" %
        (tegra_pt_logical_sector_address, tegra_pt_logical_sectors_num))

pt_start_addr = SECTOR_SIZE * tegra_pt_logical_sector_address

logical_sector_size = 2048

pt_buff = buffer[pt_start_addr:pt_start_addr+logical_sector_size]

pt = tegra_partition_table.from_buffer_copy(pt_buff)

ret = tegra_partition_table_insec_hdr_valid(pt)
if not ret:
    raise SystemExit("Failed on tegra_partition_table_insec_hdr_valid")

ret = tegra_partition_table_unencrypted(pt)
if not ret:
    raise SystemExit("Failed on tegra_partition_table_unencrypted")

ret = tegra_partition_table_sec_hdr_valid(pt)
if not ret:
    raise SystemExit("Failed on tegra_partition_table_sec_hdr_valid")

parts = []

types = {
    2: "boot_config_table",
    3: "partition_table",
    4: "bootloader",
}

partition_config = """
[partition]
name={name}
id={pid}
type={ptype}
allocation_policy=sequential
filesystem_type=basic
size={psize}
file_system_attribute=0
partition_attribute=0
allocation_attribute=8
percent_reserved=0
"""

partfile = open("mmx_part.cfg", "w")
partfile.write("""[device]
type=snor
instance=0
""")

for i in range(pt.secure.num_partitions):
    p = pt.partitions[i]
    prev = pt.partitions[max(i - 1, 0)]
    pi = p.part_info

    # if (slot == state.limit and not check_only)
    #     break;

    # sector = pilogical_sector_address);
    # size   = pilogical_sectors_num);

    ret = tegra_partition_valid(p, prev, pi.logical_sector_address, pi.logical_sectors_num)
    name, pid, sect_end, sector, size = ret
    # parts.append((name, sect_end, sector, size))
    psize = size * SECTOR_SIZE

    fname = Path(f"{name}.bin")
    fname.write_bytes(
        buffer[sector*SECTOR_SIZE: (sector+size)*SECTOR_SIZE]
    )

    ptype = types.get(pid, "data")
    partfile.write(partition_config.format(**locals()))
    if pid not in types:
        partfile.write(f"filename={fname}\n")

partfile.close()

