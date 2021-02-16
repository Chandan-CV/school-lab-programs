#Program 9
#Write a program to find the sum of series 1 + x^2/2 + x^3/3 .... x^n/n
#Name : Adeesh Devanand
#Date of Execution: July 19, 2020
#Class 11

n = int(input("Enter the number of terms"))
x = int(input("Enter the value of x"))
sum1 = 1
for i in range(2, n+1):
    sum1=sum1+((x**i)/i)
    
print("sum of series = ", round(sum1, 2))

'''Output of Prgram 9

Enter the number of terms3
Enter the value of x3
sum of series =  14.5 '''
