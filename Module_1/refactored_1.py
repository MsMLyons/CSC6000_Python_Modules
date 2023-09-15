Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = input("What is your name? ")
What is your name? Alexa
age = eval(input(f"What is your age, {name}? "))
What is your age, Alexa? 33
current_year = eval(input("What is the current year? "))
What is the current year? 2023
year1 = (current_year - 1) - age
year2 = current_year - age
print(f"Dear {name}, you were born in {year1} or {year2}.")
Dear Alexa, you were born in 1989 or 1990.
