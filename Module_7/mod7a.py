import random
from time import sleep
# import math
# use .comb function

def lotto():
    
    while True:

        print()
        game_intro = [
            "Let's play the lotto. \n",
            "Your objective is to guess the winning lottery numbers. \n",
            "Want to win big? Guess all of the numbers correctly. \n",
            "Your prize: the satisfaction of beating the computer at the random drawing! \n",
            "If you guess all but one number correctly, you win little. \n",
            "That's better than nothing at all, even if nothing is the prize! \n",
            "This lotto is free, so try as many times as you want. \n",
            "The odds are against you. Good luck! \n"
            ]
        for phrase in game_intro:
            print(phrase)
            #sleep(2)

        start_game = input("Ready to get started? Press Y to continue or any key to exit. \n")
        if start_game.lower() != "y":
            break
        else:
            print()
            lotto_card = int(input("Please enter the number of values on the lotto card, from 10 - 100: \n"))
            # add check for valid values
            if 10 <= lotto_card <= 100:
                print()
                print(f"You have selected to have {lotto_card} values on your lotto card. \n")
            else:
                # if values not valid, add prompt to request valid values
                print("Please enter a valid number of values for the lotto card. \n")
            
        # limit the maximum number of player guesses to 10% of the lotto_card value
        # max_guesses = round(lotto_card / 10)
        max_guesses = lotto_card
        # print(f"You may make {max_guesses} guesses from 1 to {lotto_card}. \n")
        print(f"You may choose from 1 to {max_guesses} values as the numbers you will play on your the lotto card. \n")

        # add an input for the number of values to be guessed out of maximum lotto_card
        num_guesses = int(input("Please enter the number of values you'd like to choose: \n"))
        # add check for valid number of player guesses
        if num_guesses <= max_guesses:
            print(f"You'd like to choose {num_guesses} values. Let's calculate the probability of matching all your chosen numbers and winning big! \n")
        else:
            # if value for the number of guesse is not valid, add prompt to request a valid number
            print("Please try again with a valid number. \n")

        # calculate probability of winning big = hitting all drawn numbers
        def comb(k, n):
            ans = 1
            for i in range(k):
                ans *= (n - i) / (i + 1)
            return ans
        
        def probability_win_big(k, n):
            total_combinations = comb(k, n)
            win_big = 1 / total_combinations            
            return win_big
        
        result1 = probability_win_big(num_guesses, lotto_card)        
        
        # print probabilities of winning big 
        print(f"The probability of winning big is: {result1} \n")

        print("Now let's calculate the probability of matching all but one of your chosen numbers. \n")

        # calculate the probability of winning little = hitting k-1 drawn numbers
        def probability_win_little(k, n):
            partial_combinations = comb(k -1, n)
            win_small = 1 / partial_combinations
            return win_small
        
        result2 = probability_win_little(num_guesses, lotto_card)

        # print probabilities of winning little
        print(f"The probability of winning little is: {result2} \n")

        print("Like those odds? Let's choose some winning numbers! \n")
        # create variable to store the list of player guesses
        guesses = []

        for i in range(num_guesses):
            # add the player_guesses input for the number of values to be guessed            
            player_guesses = int(input(f"Please enter a value for your guess, from 1 to {lotto_card}: \n"))
            # add if statement to check that player guesses fall in the range of >= 1 and <= lotto_card
            if player_guesses >= 1 <= lotto_card:
                guesses.append(player_guesses)
                print(f"You have chosen to play the numbers: {guesses}. \n")
            else:
                print("Please try again with a valid number. \n")
        

        print(guesses)   
        

            # draw the lotto
            # compare lotto draw with player_guesses
            # print feedback - You win big! / You almost got it! / Sorry, better luck next time!     

lotto()