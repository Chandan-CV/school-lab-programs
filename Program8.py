#Program 8
#Write a program to find the sum of series 1 + 1/2 + 1/3 +..... 1/N
#Name : Adeesh Devanand
#Date of Execution: July 19, 2020
#Class 11

n = int(input("Enter the number"))
sum1 = 0.0
for i in range(1, n+1):
    sum1=sum1+(1/i)
print("sum of series = ", round(sum1, 2))

'''Output of Prgram 8

Enter the number5
sum of series =  2.28 '''
