# Date: 4/6/25

import random

random_Number = (random.randrange(1,101))

def valid_number():

    while True:
        try:
            user_guess = input("Guess a number between 1-100: ")
            user_guess = int(user_guess)
            if 1 <= user_guess <= 100:
                print(f"You guessed: {user_guess}")
                user_guess = int(user_guess)
                return user_guess
                break  # valid guess — exit loop
            else:
                print("The number use guessed is out of range. Please enter a number between 1 and 100.")
        except ValueError: 
            print("Invalid input. Please enter an integer: ")

times_guessed = 0
while True:
    guess = valid_number()  # Store the returned guess
    times_guessed += 1
    if guess > random_Number:
        print("Your guess was too high! Try again!")
    elif guess < random_Number:
        print("Your guess was too low! Try again!")
    else:
        print("You guessed the number!")
        print(f"The number was {random_Number} and it took you {times_guessed} guesses to figure it out!")
        break  #  Exit the loop when guessed correct

