# import random

# print ()

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number between 1 and {x}: '))
#         if guess < random_number:
#             print('Sorry, guess again. Too low.')
#         elif guess > random_number:
#             print('Sorry, guess again. Too high.')

#     print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low  # could also be high b/c low = high
#         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1

#     print(f'Yay! The computer guessed your number, {guess}, correctly!')


# guess(10)




""" Number Guessing Game
----------------------------------------
"""
import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print ()
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello there! Welcome to the Number Guessing Game (NGG)!")
    player_name = input("What is your name please? ").upper()
    print()
    print(".....................................................................")
    wanna_play = input("Hi, {}, would you like to start playing the number guessing game? (Enter Y/N)".format(player_name))
     
    attempts = 0
    show_score()
    while wanna_play.lower() == "y":
        try:
            guess = input("Pick a number between 1 and 10: ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print()
                print(f'YEEHH!, CONGRATULATIONS. You have guessed the number {random_number} correctly!!')
                attempts += 1
                attempts_list.append(attempts)
                print(".....................................................................")
                print("It took you {} attempts".format(attempts))
                print ()
                play_again = input("Would you like to play the game again? (Enter Y/N) ").lower()
                print()
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "n":
                    print("Thank you playing the NGG, Goodbye!!")
                    break
            elif int(guess) > random_number:
                print("SORRY! Guess again, the number you guessed is greater")
                attempts += 1
            elif int(guess) < random_number:
                print("SORRY! Guess again, the number you guesed is smaller")
                attempts += 1
        except ValueError as err:
            print("Invalid input. Please try again...")
            print("({})".format(err))
    else:
        print()
        print("Thank you playing the NGG, Goodbye!!")
        print("      ~THE END~")
        print()
if __name__ == '__main__':
    start_game()