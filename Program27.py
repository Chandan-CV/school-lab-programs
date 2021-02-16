#Program 27
#Write a program to find mean of all elements in a tuple
#Name : Adeesh Devanand
#Date of Execution: September 21, 2020
#Class 11

t1 = eval(input("Enter the tuple"))
length = len(t1)
sumt = 0
for x in t1:
    sumt += x
mean = sumt/length
print(mean)

'''Output of Program 27
Enter the tuple12, 23, 34
23.0
'''
