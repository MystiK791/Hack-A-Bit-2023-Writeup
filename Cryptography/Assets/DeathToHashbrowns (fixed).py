import hashlib
import string

source = "b18f21b19e0f86b22d218c86e182214b867b36212576b2617e8c03862d369e"

source_split = [source[i:i+2] for i in range(0, len(source), 2)]

print(source_split)

def bruteForceAscii(target):
    min_index = 65
    max_index = 127
    guess = min_index
    decrypted = ''
    result = ''
    while result != target and guess <= max_index:
        decrypted = chr(guess)
        md5h = hashlib.md5(decrypted.encode('ascii'))
        result = md5h.hexdigest()[0:2]
        if result == target:
            print(result, end = "")
            return decrypted   
        else:
            guess += 1


def convertToAscii(list_of_char):
    result = []
    for i in range(len(list_of_char)):
        result.append(ord(list_of_char[i]))
    return result

def verify(list_of_char):
    for char in list_of_char:
        md5h = hashlib.md5(char.encode('ascii'))
        result = md5h.hexdigest()[0:2]
        print(result, end="")
    print("\n")

def verifyAscii(list_of_char):
    for char in list_of_char:
        chrchar = chr(char)
        md5h = hashlib.md5(chrchar.encode('ascii'))
        result = md5h.hexdigest()[0:2]
        print(result, end="")
    print("\n")

def crackOTP(knownFive, encryptedFive):
    otp = ''
    i = 0
    print(knownFive)
    print(encryptedFive)
    for i in range(len(knownFive)):
        ordEnc = ord(encryptedFive[i])
        ordKnow = ord(knownFive[i])
        print(ord(knownFive[i]))
        print(ord(encryptedFive[i]))
        otp = otp + str(ordKnow - ordEnc)
    return otp

def decryptString(encryptedString, otp):
    string = ''
    i = 0
    for i in range(len(encryptedString)):
        string = string + chr(encryptedString[i] + int(otp[i % 5]))
    return string

result_chars = []

for char in source_split:
    result_chars.append(bruteForceAscii(char))

print(result_chars)

verify(result_chars)

flag = ['f', 'l', 'a', 'g', '{']

known = []

for i in range(5):
    print(i)
    known.append(result_chars[i])

otp = crackOTP(flag, known)

print(otp)

result_ascii = convertToAscii(result_chars)
print(decryptString(result_ascii, otp)) 




        
