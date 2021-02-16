#Program 31
#Write a program to find maximum value among list of values
#Name : Adeesh Devanand
#Date of Execution: September 21, 2020
#Class 11

l = eval(input("Enter a list of values"))
maximum = l[0]
for x in l:
    if x > maximum:
        maximum = x
print("Maximum value is", maximum)

'''Output of Program31
Enter a list of values[12,3,44,3,31]
Maximum value is 44
'''
    
