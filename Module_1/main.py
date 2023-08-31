# ask for the user's name
print("What is your name? ")
name = input()

# ask for the user's age
print(f"What is your age, {name}? ")
age = int(input())

# ask for the current year
print("What is the current year? ")
current_year = int(input())

# calculate year(s) born
year1 = (current_year - 1) - age
year2 = current_year - age

# output 
print(f"Dear {name}, you were born in {year1} or {year2}.")