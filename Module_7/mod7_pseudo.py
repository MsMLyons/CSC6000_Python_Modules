# ask the value of n, which represents the lotto card values
lotto_card = int(input("Please enter the total number of values on the lotto card: "))
# ask the value of k, which represents the player guesses
guesses = []
num_guesses = int(input("Please enter the number of values you would like to guess: "))
print("You entered X guesses.")
for i in range(num_guesses):
    player_guesses = int(input("Please enter the a value: "))
guesses.append(player_guesses)
print(guesses)
# compute the probability of winning big (all player guesses matching random drawing)
# compute the probability of winning little (all but one player guesses matches the random drawing)
# randomly choose k from n, which represents the random drawing of values
# compare results and declare: win big, win little, or sorry


# probability_little = (binomial_coefficient(n, k-1) * (n - k + 1)) / binomial_coefficient(n, k)