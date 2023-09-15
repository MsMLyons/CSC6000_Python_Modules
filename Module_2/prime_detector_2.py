n = int(input("Enter a number: "))

noMultiples = True

for i in range(n-1, 1, -1):
    if(n % i) == 0:
        noMultiples = False
        break
if(noMultiples):
    print(n, "is a prime number.")
else:
    print(n, "is a composite.")

# observation: make sure indentation, or lack thereof, is correct before running the program.
