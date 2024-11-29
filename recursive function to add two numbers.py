def addition(num_1,num_2):
    if num_1==0 :
        return num_2
    elif num_2 ==0:
        return num_1
    else:
        return addition(num_1+1,num_2-1)

numb_1 = int(input("Enter a number to find its addition: "))
numb_2 = int(input("Enter second number to find its addition: "))

result = addition(numb_1,numb_2)
print(f"The addition of {numb_1} and {numb_2} is {result}")