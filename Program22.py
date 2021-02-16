#Program 22
#Write a program to create a tuple of Fibonacci series
#Name : Adeesh Devanand
#Date of Execution: September 16, 2020
#Class 11

n = int(input("Enter the length of the Fibonacci series"))
a = 0
b = 1
l = []
if n <= 0:
    print("Invalid input")
elif n >= 1:
    l.append(a)
    if n >= 2:
        l.append(b)
        if n >= 3:
            for i in range(0, n):
                c = a + b
                l.append(c)
                a = b
                b = c
print(l)
t = tuple(l)
print(t)
                

'''Output of Program22
Enter the length of the Fibonacci series4
[0, 1, 1, 2, 3, 5]
(0, 1, 1, 2, 3, 5)
'''
