'''
Description:Write a Python function to find the maximum of three numbers.
'''


def maximum_of_three_numbers(a,b,c):
    if a>b and a>c :
        print(a ,"is the maximum among three numbers.")
    elif b>a and b>c:

        print(b ,"is the maximum among three numbers.")
    else:
        print(c ,"is the maximum among three numbers.")

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))



maximum_of_three_numbers(a,b,c)