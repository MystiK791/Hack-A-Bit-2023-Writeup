filename = "bites.bin"
with open(filename,'rb') as f:
    buff = f.read() # it reads the whole file into memory


out_hex = ['{:02X}'.format(b) for b in buff]

out_hex_updated = []

a = out_hex[0]

b = out_hex[52]

print(a)
print(b)

for item in out_hex:
    out_hex_updated.append(item)

total = 0

for item in out_hex_updated:
    total += int(item, 16)
print(out_hex_updated)

print(total)
