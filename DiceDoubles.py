#-------------------------------------------------------------------------
# Name:       DiceDouble
# Purpose:    Adds the sum of 2 rolled dice
# Author:     Fung. C
# Created:    06/06/2024
#-------------------------------------------------------------------------

#Importing random
import random

#Welcome
print("HERE COMES THE DICE!")

#Important Variables
counter = 0
sum = 0

#Loop
while True:
    #Checking if counter is 3, and output its corresponding output
    if counter == 3:
        break
    else:
        roll_1 = random.randrange(1,7)
        roll_2 = random.randrange(1,7)
        sum = roll_1 + roll_2

        print(f"Roll 1: {roll_1}")
        print(f"Roll 2: {roll_2}")
        print(f"The total is {sum}!")
    
    counter += 1