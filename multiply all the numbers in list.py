'''
Description:Write a Python function to multiply all the numbers in a list.
'''
def multiply_of_all_the_numbers(a,b,c,d,e):
    total=1
    for x in a,b,c,d,e:
        total*=x
    return total



a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
d=int(input("Enter the number"))
e=int(input("Enter the number"))
multiply_of_all_the_numbers(a,b,c,d,e)
print(multiply_of_all_the_numbers(a,b,c,d,e))
