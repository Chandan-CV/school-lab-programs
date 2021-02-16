#Program 28
#Write a program to accept a new list of strings and create a new list
#containing elements of first list with their first character removed
#Name : Adeesh Devanand
#Date of Execution: September 21, 2020
#Class 11

l = eval(input("Enter the list of strings"))
l1 = []
for x in l:
    l1.append(x[1:])
print(l1)
'''Output of Program28
Enter the list of strings["Computers", 'apple', 'mac']
['omputers', 'pple', 'ac']
'''
