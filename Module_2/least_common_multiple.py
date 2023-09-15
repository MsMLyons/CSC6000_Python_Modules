n = int(input("Enter a number: "))
m = int(input("Enter another number: "))

if (n < m):
    initial = m
else:
    initial = n

for i in range(initial, (n * m) + 1):
    if ((i % n) == 0) and ((i % m) == 0):
        print("The LCM between", n, "and", m, "is", i)
        break
