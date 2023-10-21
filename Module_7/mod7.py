from time import sleep
from fractions import Fraction

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
            "The odds are against you. Good luck! \n\n"            
            ]
        for phrase in game_intro:
            print(phrase)
            sleep(1.75)

        start_game = input("Ready to get started? Press Y to continue or any key to exit. \n\n")
        if start_game.lower() != "y":
            break
        else:
            print()
            lotto_card = int(input("Please enter the number of values on the lotto card, from 10 - 100: \n\n"))
            # add check for valid values
            if 10 <= lotto_card <= 100:
                print()
                print(f"You have selected to have {lotto_card} values on your lotto card. \n\n")
            else:
                # if values not valid, add prompt to request valid values
                print("That is not a valid number of values for the lotto card. You'll have to try again later. Goodbye! \n")
                break            
    
        max_guesses = lotto_card        
        print(f"You may choose from 1 to {max_guesses} values as the numbers you will play on your the lotto card. \n\n")

        # add an input for the number of values to be guessed out of maximum lotto_card
        num_guesses = int(input("Please enter the number of values you'd like to choose: \n\n"))
        # add check for valid number of player guesses
        if num_guesses <= max_guesses:
            print()
            print(f"You'd like to choose {num_guesses} values. Let's calculate the probability of matching all your chosen numbers and winning big! \n\n")
            sleep(1.75)
        else:
            # if value for the number of guesse is not valid, add prompt to request a valid number
            print("That is not a valid number of values to guess. Please try again later with a valid number. Goodbye! \n")
            break

        # calculate probability of winning big = hitting all drawn numbers
        def comb(k, n):
            ans = 1
            for i in range(k):
                ans *= (n - i) / (i + 1)
            return ans
        
        def probability_win_big(k, n):
            total_combinations = int(comb(k, n))
            win_big = Fraction(1, total_combinations)            
            return win_big
        
        result1 = probability_win_big(num_guesses, lotto_card)        
        
        # print probabilities of winning big       
        print(f"----------*---------- The probability of winning big is: {result1.numerator} / {result1.denominator} ----------*---------- \n\n")
        sleep(1.75)
        print("Now let's calculate the probability of matching all but one of your chosen numbers. \n\n")
        sleep(1.75)

        # calculate the probability of winning little = hitting k-1 drawn numbers
        def probability_win_little(k, n):
            partial_combinations = int(comb(k - 1, n))            
            win_small = Fraction(1, partial_combinations)
            return win_small
        
        result2 = probability_win_little(num_guesses, lotto_card)

        # print probabilities of winning little
        print(f"----------*---------- The probability of winning little is: {result2.numerator} / {result2.denominator} ----------*---------- \n\n")
        sleep(1.75)
        print("Like those odds? Let's choose some winning numbers! \n\n")
        sleep(1.75)

        game_outro = [            
            "01110111 01100001 01110010 01101110 01101001 01101110 01100111",
            "01101000 01100001 01100011 01101011 01100101 01100100",
            "01110011 01111001 01110011 01110100 01100101 01101101 00100000 01100100 01101111 01110111 01101110",
            "01110111 01100001 01110010 01101110 01101001 01101110 01100111",
            "01101000 01100001 01100011 01101011 01100101 01100100",
            "01110011 01111001 01110011 01110100 01100101 01101101 00100000 01100100 01101111 01110111 01101110",            
            "                                                                                               ... \n",
            "Oh no! The lotto system has been hacked! \n",
            "Try again tomorrow once our engineers have had a chance to debug the system. \n",
            "Goodbye! \n"            
            ]
        for phrase in game_outro:
            print(phrase)
            sleep(1.75)       

        break
lotto()