import random

# TREE-HOUSE SOLUTION
def game():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            # get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print ("{} isn't a number!".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print ("You got it! My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print ("My number is higher than {}".format(guess))
            else:
                print ("My number is lower than {}".format(guess))
            guesses.append(guess)
    else:
        print ("You didn't get it! My number was {}".format(secret_num))
	

	play_again = input("Do you want to play again? Y/n ")
	if play_again.lower() != 'n':
	    game()
	else:
	    print ("Bye!")

game()

# MY SECOND ATTEMPT

# generate a random number between 1 and 10
# secret_num = random.randint(1, 10)
# no_of_guesses = 5
#
# while True:
#     # get a number guess from the player
#     try:
#         guess = int(input("Guess a number between 1 and 10: "))
#     except ValueError:
#         print ("Not a number. Please try again")
#         continue
#     else:
#         # compare guess to secret number
#         if guess == secret_num:
#             print ("You got it! My number was {}".format(secret_num))
#             break
#         else:
#             no_of_guesses -= 1
#
#             if no_of_guesses == 0:
#                 print ("You've exceeded your number of guesses.")
#                 break
#             elif guess < secret_num:
#                 print ("That's not it!. too low. {} guesses left".format(no_of_guesses))
#             elif guess > secret_num:
#                 print ("That's not it!. too high. {} guesses left".format(no_of_guesses))

# MY ATTEMPT

# generate a random number between 1 and 10
# rand_num = random.randint(1, 10)
# print (rand_num)
#
# # get a number guess from the player
# print("Guess a number between 1 and 10: ")
# guess = int(input(">> "))
#
# # compare guess to secret number
# if guess == rand_num:
#     # print hit/miss
#     print("You've got a hit!")
# else:
#     print("Sorry but that was a miss. The number was {}.".format(rand_num))