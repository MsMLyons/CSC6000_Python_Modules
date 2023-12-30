# ask for the user's name
name = input("What is your name? ")

# ask for the user's age
age = eval(input(f"What is your age, {name}? "))

# ask for the current year
current_year = eval(input("What is the current year? "))

# calculate year(s) born
year1 = (current_year - 1) - age
year2 = current_year - age

# output 
print(f"Dear {name}, you were born in {year1} or {year2}.")