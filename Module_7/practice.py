total_values = int(input("Enter the number of values on the lottery card: ")) # represents n
guesses = int(input("Enter the number of guesses: ")) # represents k

def comb(k, n):
    ans = 1
    if (k > n//2):
        k = n - k
    for i in range(k):
        ans *= (n - i) / (i + 1)
    return ans

def probability(k, n):
    total_combinations = comb(k, n)
    probability_of_winning = 1 / total_combinations
    return probability_of_winning

result = probability(guesses, total_values)
print("The probability of winning is: ", result)