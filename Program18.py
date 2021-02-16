#Program 18
#Write a program to input a number and test if it is a prime number
#Name : Adeesh Devanand
#Date of Execution: August 10, 2020
#Class 11

num = int(input("Enter a number"))
lim = int(num/2) + 1
for i in range(2, lim):
    if(num%i == 0):
        print("It is not a prime no")
        break
else:
    print("It is a prime no")

''' Output of Program18

Enter a number7
It is a prime no '''
