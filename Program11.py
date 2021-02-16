#Program 11
#Write a program to accept a number and add all the digits in that number
#Name : Adeesh Devanand
#Date of Execution: July 19, 2020
#Class 11

n = int(input("Enter the number"))
sumt=0
while(n != 0):
    sumt = sumt + (n%10)
    n = n//10
print("Sum of digits = ", sumt)

'''Output of Program11

Enter the number1234
Sum of digits =  10 '''
