'''
Author:Rayan Joomy
Date:19-10-2024
Description: Python program that performs the following tasks:

    Create two separate strings:
        The first string should contain your first name.
        The second string should contain your last name.

    Concatenate the two strings with a space in between and store the result in a new variable.

    Print the concatenated string.

    From the concatenated string:
        Access and print a sub-string that consists of the last name only.
        Use string slicing to extract the sub-string.
'''
name1=input("Enter your first name: ")
name2=input("Enter your last name: ")
name3=(name1+" "+name2)
print(name3)
name1_length=len(name1)
print(name3[name1_length:])


