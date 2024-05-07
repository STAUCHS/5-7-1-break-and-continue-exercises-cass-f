#-------------------------------------------------------------------------
# Name:       BankPIN
# Purpose:    Ensuring the right PIN is entered
# Author:     Fung. C
# Created:    06/06/2024
#-------------------------------------------------------------------------

print("** WELCOME TO STA BANK! **")

#Loop
while True:
    pin = int(input("Enter your PIN: "))
    #Checking if the PIN is right or wrong and outputing the corresponding output
    if pin == 5326:
        print("PIN accepted. You may now access your account.")
        break
    elif pin != 5326:
        print("Incorrect PIN. Try again.")