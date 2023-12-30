# Step 1 - Ask the user for a number as a string (it's ok to set a max number of digits)

user_num = input("Please enter a number: ")

# Step 2 - Ask which is the base (an integer from 2 to 16)

base = int(input("Please enter an integer from 2 to 16 as the base: "))

# Step 3 - Compute the binary and decimal representations of the number 

newNum1 = int(user_num, base)
newNum2 = bin(newNum1)

# Step 4 - Print the computations as a string

print(f"{user_num} in base {base} is: {newNum1} in base 10 and {newNum2[2:]} in base 2.")