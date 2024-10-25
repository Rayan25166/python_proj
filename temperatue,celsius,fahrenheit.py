
temp1=int(input("Enter the temperature"))
scale= input(" is this in (c)elcius or (f)ahrenheit?")

if scale=="c":
    f=(9/5*temp1)+32
    print(temp1 , "Celsius is ",f,"Fahrenheit")

if scale=="f":
    c = 5/9*(temp1-32)
    print(temp1,"Fahrenheit is",c,"Celsius.")

