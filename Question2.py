#-------------------------------------------------------------------------
# Name:       Question 2
# Purpose:    Loop adding numbers from 5 to 20, but not multiples of 3
# Author:     Fung. C
# Created:    06/06/2024
#-------------------------------------------------------------------------

#Establishing variables
num = 4
sum = 0

while True:
    num += 1
    #Checking if num moduel 3 is 0, if num smaller than 20 and if num is equal to 20 and outputing its corresponding output
    if (num % 3) == 0:
        continue
    elif num < 20:
        sum += num
    elif num == 20:
        sum += num
        print(sum)
        break