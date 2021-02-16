#Program 10
#Write a program to find the sum of series 1 + x + x^2 + x^3 +.... x^n
#Name : Adeesh Devanand
#Date of Execution: July 19, 2020
#Class 11

n = int(input("Enter the number of terms"))
x = int(input("Enter the value of x"))
sum1 = 1
for i in range(1, n+1):
    sum1=sum1+(x**i)
    
print("sum of series = ", round(sum1, 2))

'''Output of Prgram 10

Enter the number of terms5
Enter the value of x2
sum of series =  63 '''
