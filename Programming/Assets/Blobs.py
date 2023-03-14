x = int(input("Enter the initial X value: "))
y = int(input("Enter the initial Y value: "))
coords = input("Enter the string of movements: ")
coords = coords.replace(' ', '')

for char in coords:
    match char:
        case '↑':
            y += 1
        case '↗':
            x += 1
            y += 1
        case '→':
            x += 1
        case '↘':
            x += 1
            y -= 1
        case '↓':
            y -= 1
        case '↙':
            x -= 1
            y -= 1
        case '←':
            x -= 1
        case '↖':
            x -= 1
            y += 1
        case ' ':
            x += 0
            y += 0
        
print(x)
print(y)
