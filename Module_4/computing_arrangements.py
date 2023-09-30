def fact(n):
    acc = 1
    for i in range(2, n + 1):
        acc *= i
    return acc

def arrangement(k, n):
    return fact(n) // fact (n-k)

def arrange(k, n):
    ans = 1
    for i in range(n, n-k, -1):
        ans *= i
    return ans

for n in range(3, 8):
    for k in range(1, n + 1):
        print(k, "{} elements out of {} is {}".format(k, n, arrange(k, n)))
    print("-----")

# result -->

# 1 1 elements out of 3 is 3
# 2 2 elements out of 3 is 6
# 3 3 elements out of 3 is 6
# -----
# 1 1 elements out of 4 is 4
# 2 2 elements out of 4 is 12
# 3 3 elements out of 4 is 24
# 4 4 elements out of 4 is 24
# -----
# 1 1 elements out of 5 is 5
# 2 2 elements out of 5 is 20
# 3 3 elements out of 5 is 60
# 4 4 elements out of 5 is 120
# 5 5 elements out of 5 is 120
# -----
# 1 1 elements out of 6 is 6
# 2 2 elements out of 6 is 30
# 3 3 elements out of 6 is 120
# 4 4 elements out of 6 is 360
# 5 5 elements out of 6 is 720
# 6 6 elements out of 6 is 720
# -----
# 1 1 elements out of 7 is 7
# 2 2 elements out of 7 is 42
# 3 3 elements out of 7 is 210
# 4 4 elements out of 7 is 840
# 5 5 elements out of 7 is 2520
# 6 6 elements out of 7 is 5040
# 7 7 elements out of 7 is 5040
# -----