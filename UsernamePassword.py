#-------------------------------------------------------------------------
# Name:       UsernamePassword
# Purpose:    Asking for username and password to login
# Author:     Fung. C
# Created:    06/06/2024
#-------------------------------------------------------------------------

#Looping
while True:
    #Asking user for the username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    #Checking if the username and password is right, and if so outputing the corresponding output
    if username != 'StAugustineCHS' and password != 'Coding123!':
        print("Username and password incorrect.")
    elif username == 'StAugustineCHS' and password != 'Coding123!':
        print("Password incorrect.")
    elif username != 'StAugustineCHS' and password == 'Coding123!':
        print("Username incorrect.")
    elif username == 'StAugustineCHS' and password == 'Coding123!':
        print("Welcome!")
        break