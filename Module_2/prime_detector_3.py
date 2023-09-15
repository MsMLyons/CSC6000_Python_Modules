n = int(input("Enter a number: "))

noMultiples = True

for i in range(n//2, 1, -1):
    if (n % i) == 0:
        noMultiples = False
        break
if (noMultiples):
    print(n, "is a prime.")
else:
    print(n, "is a composite.")
