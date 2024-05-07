#-------------------------------------------------------------------------
# Name:       Question 1
# Purpose:    Printing numbers 0 to 7, skipping the number 7
# Author:     Fung. C
# Created:    06/06/2024
#-------------------------------------------------------------------------

#Establishing base number
num = 0

#Looping
while True:
    num += 1
    #Checking if the number is 11, not equal to 7, or equal to 7 and outputing the corresponding output
    if num == 11:
        break
    elif num != 7:
        print(num)
    elif num == 7:
        continue