#-------------------------------------------------------------------------
# Name:       Question 4
# Purpose:    Infinite loop until you say stop
# Author:     Fung. C
# Created:    06/06/2024
#-------------------------------------------------------------------------

#Loop
while True:
    word = input("Enter a word: ")
    #Checking if the word 'stop' is entered, and printing its corresponding output
    if word == 'stop':
        print("Goodbye!")
        break
    else:
        print(f"Your word: {word}")
