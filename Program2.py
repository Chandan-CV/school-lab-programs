#Program 2
#Write a program to accept 2 numbers and interchange the values without using a temporary variable
#Name : Adeesh Devanand
#Date of Execution: July 17, 2020
#Class 11

a = int(input("Enter first number"))
b = int(input("Enter second number"))
a = a + b
b = a - b
a = a - b
print("Interchanged value of the first number is", a)
print("Interchanged value of the second number is", b)

'''Output of Program 2

Enter first number3
Enter second number5
Interchanged value of the first number is 5
Interchanged value of the second number is 3'''
