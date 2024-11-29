def side_of_triangle():
    a=int(input("Enter the  first side of triangle:"))
    b=int(input("Enter the second side of triangle:"))
    c=int(input("Enter the third side of triangle:"))
    pythagorean_theorem=(a**2+b**2)
    if pythagorean_theorem==c**2:
        print("It is a right angled triangle")

    else:
        print("It is not a right angled triangle")
side_of_triangle()








