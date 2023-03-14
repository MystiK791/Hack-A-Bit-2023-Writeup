n = 83242763

p = 1
q = 1

for i in range(83242763):
    for j in range(83242763):
        if (p * q) == n and p != 83242763 and q != 83242763:
            print(p)
            print(q)
            break
        p += 1
    p = 1
    q += 1
