#Program 15
#Write a program to accept a year and check if it is a leap year or not
#Name : Adeesh Devanand
#Date of Execution: July 19, 2020
#Class 11

year = int(input("Enter the year"))
if year % 100 == 0:
    if year % 400 == 0:
        print("It is a leap year")
    else :
        print("It is not a leap year")
elif year % 4 == 0:
    print("It is a leap year")
else :
    print("It is not a leap year")

'''Output of Program15

Enter the year1904
It is a leap year '''
