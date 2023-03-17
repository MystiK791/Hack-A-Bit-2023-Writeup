from numpy import loadtxt, sort

data = loadtxt('speed.txt')

print(data)

sorted_numbers = sort(data)

print(sorted_numbers[52133])
