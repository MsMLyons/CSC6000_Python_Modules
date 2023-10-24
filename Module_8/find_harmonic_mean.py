def find_harmonic_mean(arr, n):
    sum = 0
    for i in range(0, n):
        sum = sum + (1) / arr[i]
    return n / sum

arr = [6, 4]
n = len(arr)
print(find_harmonic_mean(arr, n))

# source: https://www.geeksforgeeks.org/program-harmonic-mean-numbers/

# sample output: 4.800000000000001