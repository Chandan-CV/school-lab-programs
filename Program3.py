#Program 3
#Write a program to find area of a triangle
#Name : Adeesh Devanand
#Date of Execution: July 17, 2020
#Class 11

import math

a=int(input("Enter the first side"))
b=int(input("Enter the second side"))
c=int(input("Enter the third side"))

s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle =", area)

'''Output of Program 3

Enter the first side13
Enter the second side12
Enter the third side5
Area of triangle = 30.0 '''
