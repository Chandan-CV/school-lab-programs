#Program 13
#Write a program to find the factorial of a number using while loop
#Name : Adeesh Devanand
#Date of Execution: July 19, 2020
#Class 11

inp = int(input("Enter the number"))
n = inp
sumt = 1

while(n >= 1):
    sumt = sumt*n
    n  = n-1

print("Factorial of the number", inp, "= ", sumt)

'''Output of Pragram13

Enter the number5
Factorial of the number 5 =  120 '''
