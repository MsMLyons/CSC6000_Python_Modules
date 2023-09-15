a, b, c = 56, 34, 22


if (a > b):
    print("a is greater than b")
    

if (a < b):
    print("a is smaller than b")
else:
    print("a is greater than or equal to b")
    

if (a < b + c):
    print("a is smaller than b and c added together")
elif (b >= c):
    print("a is greater than b and c added together, and b is greater than or equal to c")
else:
    print("a is greater than b and c added together, and b is smaller than c")


# result:
# a is greater than b
# a is greater than or equal to b
# a is greater than b and c added together, and b is greater than or equal to c
