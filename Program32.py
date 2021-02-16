#Program 32
#Write a program to find a given value among list of values
#Name : Adeesh Devanand
#Date of Execution: September 23, 2020
#Class 11

l = eval(input("Enter the list to be searched"))
val = input("Enter the value to be found")

for x in range(0, len(l)):
    if l[x] == val:
        print("Value found at index", x)
        break
else:
    print("Value not found")
'''Output Of Program32
Enter the list to be searched["Comp", "is", 'f','u','n',1,2,33]
Enter the value to be foundis
Value found at index 1
'''
