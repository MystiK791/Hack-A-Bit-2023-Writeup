fileChoice = input("Enter a file to analyze: ")
stringSearch = input("Enter a string to search for: ")

with open(fileChoice) as f:
    lines = [inLine.rstrip() for inLine in f]

hitCounter = 0

for line in lines:
    if stringSearch in line:
        hitCounter += 1


print("The string " + stringSearch + " was found " + str(hitCounter) + " time(s).")
