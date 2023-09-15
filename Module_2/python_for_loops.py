# FOR LOOPS & RANGE

for i in [0, 1, 2, 3, 4]:
    print(i)
# result --> prints all items in the array
    

seq = [33, 66, 99, 132, 155]
for i in seq:
    print(i)
# result --> prints all items in the array

# STOP

for i in range(15):
    print(i)
# result --> prints all items in the range 0 - 14 (excludes 15, the stop index position)


print(range(5))
# result --> range(0, 5)

for i in range(5):
    print(i)
# result --> prints 0 - 4 (excludes 5)


print(range(11))
# result --> range(0, 11)

for i in range(11):
    print(i)
# result --> prints 0 - 10 (excludes 11)
    

# START / STOP

print(range(1, 11))
# result --> range(1, 11)

for i in range(1, 11):
    print(i)
# result --> prints 1 - 10 (excludes 0, 11)


print(range(5, 15))
# result --> range(5, 15)

for i in range(5, 15):
    print(i)
# result --> prints 5 - 14 (excludes 0 - 4, 15)


print(range(-2, 4))
# result --> range(-2, 4)

for i in range(-2, 4):
    print(i)
# result --> prints [-2, -1, 0, 1, 2, 3], (excludes 4)


# START / STOP / STEP

print(range(1, 10, 2))
# result --> range(1, 10, 2)

for i in range(1, 10, 2):
    print(i)
# result --> [1, 3, 5, 7, 9]


print(range(1, 11, 2))
# result --> range(1, 11, 2)

for i in range(1, 11, 2):
    print(i)
# result --> [1, 3, 5, 7, 9]


print(range(9, -1, -1))
# result --> range(9, -1, -1)

for i in range(9, -1, -1):
    print(i)
# result --> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


print(range(15, 3, -3))
# result --> range(15, 3, -3)

for i in range(15, 3, -3):
    print(i)
# result --> [15, 12, 9, 6]


for v in [1, 9, 2, 6, 0, 5, 3, 8, 4, 7]:
    print(v)
# result --> prints [1, 9, 2, 6, 0, 5, 3, 8, 4, 7]


a = [5, 3, 8, 4, 7, 1, 9, 2, 6, 0]
for v in a:
    print(v)
# result --> prints [5, 3, 8, 4, 7, 1, 9, 2, 6, 0]


for c in "definite_loop":
    print(c)
# result --> prints "definite_loop"


a = [3, 2, 5, 6, 9, 4, 8, 0, 7, 1]
for i in range(10):
    print(a[i])
# result --> prints [3, 2, 5, 6, 9, 4, 8, 0, 7, 1]


a = [3, 2, 5, 6, 9, 4, 8, 0, 7, 1]
for v in range(9, -1, -1):
    print("right here", a[i])
# result --> prints "right here 1" 10 times

for v in range(9, -1, -1):
    print(i, "this one")
# result --> prints "9 this one" 10 times


for v in range(10):
    print(v)
# result --> prints 0 - 9


for v in range(0, 20, 2):
    print(v)
# result --> prints [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


for v in range(5):
    for w in range(4):
        print(v, w)
# result --> prints two columns of numbers;
# the first column contains 0 - 4, each repeated 4 times before the next number
# the second column contains 0 - 3, repeated as a set 5 times

