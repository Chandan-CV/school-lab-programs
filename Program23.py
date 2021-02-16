#Program 23
#Write a program to check if an element is present in a tuple
#and print it's index if it is present
#Name : Adeesh Devanand
#Date of Execution: September 16, 2020
#Class 11

t = ("ABC",1, 2, "12", 'c')
val = input("Enter the value to be found")

for x in range(0, len(t)):
    if t[x] == val:
        print("Value found at index", x)
        break
else:
    print("Value not found")
'''Output Of Program23
Enter the value to be founda
Value not found
'''
