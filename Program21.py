#Program 21
#Write a program to read a line abd check if it is a palandrome
#Name : Adeesh Devanand
#Date of Execution: August 24, 2020
#Class 11

inp = input("Enter the word")
reverse = inp[::-1]
if  inp != reverse:
    print("It is not a palandrome")
else :
    print("It is a palandrome")
'''Output of Program21
Enter the wordaooa
It is a palandrome
'''
