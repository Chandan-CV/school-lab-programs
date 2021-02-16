#Program 30
#Write a program to rotate a list
#Name : Adeesh Devanand
#Date of Execution: September 21, 2020
#Class 11

l = eval(input("Enter a list"))
temp1 = l[0]
temp2 = None
print("List before rotating")
print(l)
for x in range(0, len(l)-1):
    temp2 = l[x+1]
    l[x+1] = temp1
    temp1 = temp2
else:
    l[0] = temp2
print("List after rotating")
print(l)

'''Output of Program30
Enter a list[1,2,3,4,5,6,7,8,9]
List before rotating
[1, 2, 3, 4, 5, 6, 7, 8, 9]
List after rotating
[9, 1, 2, 3, 4, 5, 6, 7, 8]
'''
