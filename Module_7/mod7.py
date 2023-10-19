import random
from time import sleep

# def intro():
#     print()
#     game_intro = [
#         "Let's play the lotto.",
#         "Your objective is to guess the winning lottery numbers.",
#         "Want to win big? Guess all of the numbers correctly.",
#         "Your prize: the satisfaction of beating the computer at the random drawing!",
#         "If you guess all but one number correctly, you win little.",
#         "That's better than nothing at all, even if nothing is the prize!",
#         "This lotto is free, so try as many times as you want.",
#         "The odds are against you. Good luck!"
#         ]
#     for phrase in game_intro:
#         print(phrase)
#         #sleep(2)

# intro()

def lotto():
    
    while True:

        print()
        game_intro = [
            "Let's play the lotto.",
            "Your objective is to guess the winning lottery numbers.",
            "Want to win big? Guess all of the numbers correctly.",
            "Your prize: the satisfaction of beating the computer at the random drawing!",
            "If you guess all but one number correctly, you win little.",
            "That's better than nothing at all, even if nothing is the prize!",
            "This lotto is free, so try as many times as you want.",
            "The odds are against you. Good luck!"
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
                print(f"You have selected {lotto_card} values on your lotto card. \n")
            else:
                # if values not valid, add prompt to request valid values
                print("Please enter a valid number of values for the lotto card. \n")
            
        # limit the maximum number of player guesses to 10% of the lotto_card value
        max_guesses = round(lotto_card / 10)
        print(f"You may make {max_guesses} guesses from 1 to {lotto_card}. \n")
        
        # add an input for the number of values to be guessed out of maximum lotto_card
        num_guesses = int(input("Please enter the number of guesses you'd like to make: \n"))
        # add check for valid number of player guesses
        if num_guesses <= max_guesses:
            print(f"You'd like to make {num_guesses} guesses. Let's choose some winning numbers! \n")
        else:
            # if value for the number of guesse is not valid, add prompt to request a valid number
            print("Please try again with a valid number. \n")

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

            # calculate the probability of winning big = hitting all drawn numbers
            # calculate the probability of winning little = hitting k-1 drawn numbers
            # print probabilities of winning big and little

            # draw the lotto
            # compare lotto draw with player_guesses
            # print feedback - You win big! / You almost got it! / Sorry, better luck next time!     

lotto()