def comb(k, n):

    ans = 1
    for i in range(n, n-k, -1):
        ans *= i
    for i in range(2, k + 1):
        ans /= i
    return ans

result = comb(150, 200)
# try: 
# 2, 5 --> 10.0
# 3, 6 --> 20.0
# 4, 8 --> 70.0
# 5, 12 --> 792.0
# 6, 10 --> 210.0
# 7, 12 --> 792.0
print("The result is", result)