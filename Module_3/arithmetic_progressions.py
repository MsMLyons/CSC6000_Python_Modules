#Arithmetic Progressions

# The nth element of an arithmetic progression

# a1 = initial term
# d = common difference

# a1 = 3
# d = 3
# n = 15
# see print(n_th)

def n_th(a1, d, n):
    return a1 + (n-1) * d

# n_th(3, 3, 15)
# runs but doesn't show output

print(n_th(45, 7, 59), "Wow that is cool")
# begin at 3, add 3 each step, stop at 15th index location
# printed 45

# print(n_th)
# when using pre-defined variables and printing the function:
# result --> <function n_th at 0x0000029F782A04A0>

print("The 15th element is:", n_th(9, 2, 15))
# begin at 9, add 2 each step, stop at 15th index location
# result --> The 15th element is: 37


# Gaussian computation: the sum of a1 = 1 and d = 1 in arithmetic progression

def sum(k):
    acc = 0
    for i in range(1, k + 1):
        acc += i
    print("The sum of 1 to", k, "is", acc, "Excellent!")

sum(40)
# result --> The sum of 1 to 20 is 210
# The sum of 1 to 40 is 820 Excellent!

def sum_1(k):
    print("The sum of 1 to", k, "is", (k * (k + 1)) // 2)

sum_1(33)
# result --> The sum of 1 to 33 is 561


# Sum of terms of any arithmetic progression

# def n_th_1(a1, d, n):
    # return a1 + (n-1) * d

def sum_2(a1, d, n):
    acc = (a1 + n_th(a1, d, n)) * n / 2
    print("The sum is: ", acc, "You did it!")

sum_2(0.23, 0.1, 10)
# result --> The sum is:  80.0
# why? --> sum of the terms in the progression: 4 + 10 + 16 + 22 + 28 

def sum_3(a1, d, n):
    acc = 0
    term = a1
    for i in range(n):
        acc += term
        term += d
    print("The sum is:", acc)

sum_3(2, 7, 3)
# result --> The sum is: 27
# why? --> sum of the terms in the progression: 2 + 9 + 16


# Summation (Sigma)

acc = 0
for i in range(100):
    acc +=2 * i + 17 # both range and d could be any number
print("The sum is:", acc)
# result --> The sum is: 11600

for i in range(7, 3, 5):
    print(i)