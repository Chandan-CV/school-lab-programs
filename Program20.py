#Program 20
#Write a program to read a line 
#Name : Adeesh Devanand
#Date of Execution: August 24, 2020
#Class 11

inp = input("Enter the line")
no_UC = 0 
no_LC = 0
no_D = 0
no_A = 0
for char in inp:
    if char.isupper():
        no_UC += 1
        no_A  += 1
    elif char.islower():
        no_LC += 1
        no_A += 1
    elif char.isdigit():
        no_D += 1

print("Then no of upper case letters are ", no_UC)
print("Then no of lower case letters are ", no_LC)
print("Then no of alphabets are ", no_A)
print("Then no of digits are ", no_D)

'''Output of Program20
Enter the lineHi, 1234aBc
Then no of upper case letters are  2
Then no of lower case letters are  3
Then no of alphabets are  5
Then no of digits are  4 '''
