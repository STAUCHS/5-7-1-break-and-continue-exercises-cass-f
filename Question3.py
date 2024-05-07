#-------------------------------------------------------------------------
# Name:       Question 3
# Purpose:    Asking user for start and end number. Adding the sum of the numbers stopping if the sum is 13 or 31
# Author:     Fung. C
# Created:    06/06/2024
#-------------------------------------------------------------------------

#Asking user for start and end point
start_point = int(input("Enter a starting point: "))
end_point = int(input("Enter an ending point: "))

#Variable sum, for the sum
sum = 0

#Looping
while True:
    #Checking if start_point is equal to end_point, and doing its corresponding code or output
    if start_point != end_point:
        sum += start_point
        #If the current number is equal to 13 or 31, it prints the sum and stops looping
        if start_point == 13 or start_point == 31:
            print(sum)
            break
    elif start_point == end_point:
        sum += start_point
        print(sum)
        break

    start_point += 1
    