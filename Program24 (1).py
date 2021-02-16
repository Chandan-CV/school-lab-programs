#Program 24
#Write a program to accept the index and print
#the value present at that location
#Name : Adeesh Devanand
#Date of Execution: September 16, 2020
#Class 11

t = ("ABC",1, 2, "12", 'c')
ind = int(input("Enter the index in forward indexing"))

for x in range(0, len(t)):
    if x == ind:
        print("Value at index", x , 'is', t[x])
        break
else:
    print("Index out of range")
'''Output Of Program24
Enter the index in forward indexing3
Value at index 3 is 12
'''
