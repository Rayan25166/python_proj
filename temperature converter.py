
'''
Author: Rayan Joomy
Date: 28-10-2024
Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:

    Convert Celsius to Fahrenheit
    Convert Fahrenheit to Celsius
    Exit the program
'''

while True:
    print("1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit the program")
    choice=int(input("Enter your choice: "))
    if choice==1:
        temp=float(input("Enter the temperature in Celsius: "))
        print((temp * 9/5) + 32,"F")
    elif choice==2:
        temp = float(input("Enter the temperature in Fahrenheit: "))
        print(((temp - 32) * 5 / 9), "C")
    elif choice==3:
        print("Exiting the program")
        break
    else:
        print("Incorrect Entry")









