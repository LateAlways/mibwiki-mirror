import zlib
from pathlib import Path

bu = Path('MU1433-MMX_fs0.bin').read_bytes()

s2p = Path('STAGE2_PRIMARY.bin').read_bytes().rstrip(b'\xFF')
bl = Path('STAGE1_RECOVERY.bin').read_bytes().rstrip(b'\xFF')
s2r = Path('STAGE2_RECOVERY.bin').read_bytes().rstrip(b'\xFF')
pt = Path('PT.bin').read_bytes().rstrip(b'\xFF')
# kn = Path('KERNEL_RECOVERY.bin').read_bytes().rstrip(b'\xFF')
kn = Path('KERNEL_PRIMARY.bin').read_bytes().rstrip(b'\xFF')
kn_content = Path('KERNEL_RECOVERY.raw.bin').read_bytes().rstrip(b'\xFF')
# kn = Path('eifs_MHI2_ER_VWG11_K3342_MU1427.img').read_bytes().rstrip(b'\xFF')

read = Path('read4.bin').read_bytes().rstrip(b'\xFF')

# kn_header = kn[0:0x8]
# kn_header += b'\x00'*(0x800 - 8)
kn_header = bytearray(kn[0:0x800])
kn_header[0:8] = b'ANDROID!'
# kn_header[0x800-4:0x800] = b'\x00\x00\x00\x00'
# kn_header[8:12] = b'\x00\x00\x00\x00'
# kn_header[12:16] = b'\x00\x00\x00\x00'
assert kn_header[13] == 8
# kn_header[13] = 4
# kn_header[37] = 4
# kn_content = zlib.decompress(kn[0x800:])
knd = kn_header + kn_content

Path('KERNEL_RECOVERY_RAW.bin').write_bytes(knd)


bulk_start = 0x80008000
# bulk_start = 0x83a08000

# s2p_address = 0x80108000
bl_address  = 0x84008000
gap_address  = 0x84018c30  # 0x84018c90
# 0x84018c90
# 0x84019be8
# 0x84019c0c checks for 0
pt_header = 0x8401c2f8
pt_address  = 0x8401c300  # verified, needs 0x01 @ 0x8401c2f8
# jump addr: 0x8401c350
s2r_address = 0x84063000
knd_address  = 0x8406B30F


gap_data = read[gap_address-bl_address:pt_header-bl_address]

# TEGRA_SNOR_BASE = 0x70009000
# pattern = bytearray([0x7C,0x68,0x01,0x84,0x00,0x90,0x00,0x70])  # need to match the bytes beforehand too
# if pattern not in bu:
	# raise SystemExit("wrong pattern")
# bu = bu.replace(pattern, pattern[0:4] + bulk_start.to_bytes(4, byteorder='little'))
# bl = bl.replace(TEGRA_SNOR_BASE.to_bytes(4, byteorder='little'), bulk_start.to_bytes(4, byteorder='little'))

partitions = [
	# (bulk_start, len(bu), bu, "MU1433-MMX_fs0"),
	# (bulk_start, len(kn_content), kn_content, "kn_content"),
	# (bl_address, len(read), read, "read"),
	(bl_address, len(bl), bl, "STAGE1_RECOVERY"),
	# (gap_address, len(gap_data), gap_data, "GAP"),
	# (pt_header, 1, b'\x01', "PT Header"),
	# (pt_address, len(pt), pt, "PT"),
	(s2r_address, len(s2r), s2r, "STAGE2_RECOVERY"),
	(knd_address, len(knd), knd, "KERNEL"),
]

start = partitions[0][0]
end = partitions[-1][0] + partitions[-1][1]

data = bytearray(end-start)

print("Length:", len(data))

print(f"| {'partition':18} | addr       | end        |")
print( "|--------------------|------------|------------|")
for addr, length, pdat, name in partitions:
	s = addr - start
	e = s+length
	data[s:e] = pdat[:]
	print(f"| {name:18} | 0x{addr:08x} | 0x{addr+length:08x} |")

# pad = s2_address - bl_addr - len(bl)
# print(f"Padding by {pad}")
# bl += bytearray(pad) + s2

# pad = kn_load - bl_addr - len(bl)
# print(f"Padding by {pad}")
# if pad < 0:
# 	bl = bl[:pad]
# else:
# 	bl += bytearray(pad)
# bl += kn_header + kn_content

Path('both.bin').write_bytes(data)