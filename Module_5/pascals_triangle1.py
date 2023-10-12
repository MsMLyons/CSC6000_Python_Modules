def comb(k, n):
    ans = 1
    for i in range(k):
        ans *= (n - i) / (i + 1)  # is there a problem on this line?
    return ans

n = 5
for i in range(1, n+1):
    for j in range(n-i+1):
        print(' ', end='')
    for j in range(1, i+1):
        print(' ', comb(i, j), sep='', end='')
    print()