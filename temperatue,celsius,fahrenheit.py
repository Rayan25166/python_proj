'''
Name:Rayan Joomy
Date:25-10-2024
Description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. 
The user should be able to input a temperature in Celsius or Fahrenheit, 
and the program should convert it to the other unit using the formula:
'''
temp1=int(input("Enter the temperature"))
scale= input(" is this in (c)elcius or (f)ahrenheit?")

if scale=="c":
    f=(9/5*temp1)+32
    print(temp1 , "Celsius is ",f,"Fahrenheit")

if scale=="f":
    c = 5/9*(temp1-32)
    print(temp1,"Fahrenheit is",c,"Celsius.")

