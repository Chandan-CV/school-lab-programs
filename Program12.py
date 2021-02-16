#Program 12
#Write a program to find if the entered number is Armstrong or not
#Name : Adeesh Devanand
#Date of Execution: July 19, 2020
#Class 11

s= input("enter the number ")
length=(len(s))
n = int(s)
sumt=0
temp=n
while(temp>0):
    rem= temp%10
    sumt= sumt+rem**length
    temp= temp//10
    

if(sumt==n):
    print("armstrong")
else:
    print("not an amstrong number")
    
'''Outout of Program12
Enter the number153
It is an armstrong no

Enter the number152
It is not an armstrong no
'''
