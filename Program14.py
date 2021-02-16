#Program 14
#Write a program to accept the total number of days and calculate its equal to
#how many years, months and days. (Assume each year to have 365 days and each month
#has 30 days
#Name : Adeesh Devanand
#Date of Execution: July 19, 2020
#Class 11

days = int(input("Enter the number of days"))
remainder = days%365
y = days//365
m = remainder//30
d = remainder%30

print("Total no of years = ", y)
print("Total no of months = ", m)
print("Total no of days = ", d)

''' Output of Program14

Enter the number of days200
Total no of years =  0
Total no of months =  6
Total no of days =  20 '''
