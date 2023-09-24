# Geometric Progressions 

# The nth element of a geometric progression

# r = common ratio
# r used in place of d (common difference) in artthmetic progression

def n_th(a, r, n):
    return a * r ** (n-1)

print(n_th(3, 2, 14), "Words of encouragement")
# result --> 


# Sum of terms of a geometric progression

# Example 1

def sum(a, r, n):
    acc = 0
    for i in range(n):
        acc += n_th(a, r, i + 1)
    print("The sum is:", acc, "🎉 Wow 🎉")

sum(3, 2, 9)
# result --> The sum is: 1533


# Example 2

def sum_1(a, r, n):
    if (r == 1):
        print("The sum is:", a * n, "🎯")
    elif (r == -1):
        print("The sum is:", a, "🚀")
    else:
        print("Use another formula 🧮")

sum_1(4, 7, 8)
# result --> Use another formula

sum_1(4, 1, 8)
# result --> The sum is: 32

sum_1(7, -1, 8)
# result --> The sum is: 7


# Example 3

def sum_2(a, r, n):
    if ( r == 1 ):
        print("The sum is:", a * n, "☄️")
    elif ( r == -1 ) and ( n % 2 == 1):
        print("The sum is:", a, "✨")
    elif ( r == -1 ) and ( n % 2 == 0):
        print("The sum is:", 0, "💥")
    else:
        print("Use another formula 🔮")

sum_2(3, 5, 22)
# result --> Use another formula 🔮

sum_2(3, 1, 22)
# result --> The sum is: 66 ☄️

sum_2(3, -1, 22)
# result --> The sum is: 0 💥

sum_2(3, -1, 23)
# result --> The sum is: 3 ✨



# Example 4 - r must be greater than 1

def sum_3(a, r, n):
    print("The sum is:", a * (r ** n - 1) / (r - 1), "🍧")

sum_3(3, 2, 23)
# result --> The sum is: 25165821.0 🍧

# Example 5 - is r less than 1?

def sum_infinity(a, r):
    if ( -1 > r > 1 ):
        print("The sum is:", a / (1 - r))
    else: 
        print("The sum is infinite")

sum_infinity(5, 0.5)
# result --> The sum is infinite
# result --> the answer is always "The sum is infinite"

sum_infinity(5, 2)
