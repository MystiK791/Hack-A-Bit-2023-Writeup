import jwt

target = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxMjM0NTY3ODkwLCJhZG1pbiI6ZmFsc2V9.QR_da_OHe58LBwBRt5S_aTcbMkBhEFqJkFn7zUq7Yyc'

rawData = {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1234567890,
    "admin": False
}

rockYou = []

with open('rockyou.txt', 'r', encoding='ANSI') as f:
    for line in f:
        rockYou.append(line.strip())
    
foundKey = ''

tries = 0

for secret in rockYou:
    tries += 1
    encoded = jwt.encode(rawData, secret, algorithm = 'HS256')
    if encoded == target:
        foundKey = secret
        print(encoded + " " + target)
        break

print("The signature was " + foundKey + ". Found after " + str(tries) + " tries.")
