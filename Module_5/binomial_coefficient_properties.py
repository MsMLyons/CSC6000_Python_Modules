def comb(k, n):
    ans = 1
    if (k > n//2):
        k = n - k
    for i in range(k):
        ans *= (n - i) / (i + 1)
    return ans

result = comb(3, 9)
print("The result is ", result)
# result --> The result is  84.0