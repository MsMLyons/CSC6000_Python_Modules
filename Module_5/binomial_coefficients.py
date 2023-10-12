def comb(k, n):
    ans = 1
    for i in range(k):
        ans *= (n-i) / (i + 1)
    return ans

result = comb(3, 9)
print("The result is: ", result)
# 3, 9 --> The result is:  84.0