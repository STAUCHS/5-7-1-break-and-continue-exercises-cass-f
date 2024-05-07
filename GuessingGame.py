#-------------------------------------------------------------------------
# Name:       GuessingGame
# Purpose:    The best guessing game ever
# Author:     Fung. C
# Created:    06/06/2024
#-------------------------------------------------------------------------

#Import random
import random

#Welcome
print ("** Guess the Number **")
print("Welcome to the best guess the number game ever!")
print("You have 5 chances to guess the number between 1 and 100.")

#Important variables
counter = 0
num = random.randrange(1, 101)

#Loop
while True:
    counter += 1
    guess = int(input("Enter a number between 1 and 100: "))
    #Checking if either the number is right, too high, or too low and checking if the number of tries is ran out and outputing its corresponding output.
    if guess == num:
        print("Correct!")
        break
    elif counter == 5:
        print(f"Sorry, you ran out of tries. The number was {num}")
        break
    elif guess < num:
        print("Too low, guess again.")
    elif guess > num:
        print("Too high, guess again.")