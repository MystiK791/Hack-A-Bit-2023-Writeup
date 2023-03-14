from pwn import *
import time

conn = remote('strfjebijc.qualifier.hackabit.com', 54321)


test = []

byte = conn.recvuntil(b'total:', drop = False)

time.sleep(2)

test.append(byte.decode())

letters = test[0].split("\n")

numbers = []

for string in letters:
    try:
        numbers.append(int(string))
    except:
        null = 0

total = 0

for number in numbers:
    total += number

print(total)

stringtotal = str(total)

print(stringtotal)

payload = bytes(stringtotal, "ascii")

flag = conn.send(bytes(stringtotal, "ascii"))

print(flag)
