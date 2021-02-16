#Program 16
#Write a program to accept two numbers and find their GCD and LCM
#Name : Adeesh Devanand
#Date of Execution: August 3, 2020
#Class 11

no1 = int(input("Enter number 1"))
no2 = int(input("Enter number 2"))
GCD = 1
x = 1
while(x <= no1 and x<= no2):
    if(no1%x==0 and no2%x==0):
        GCD = x
    x += 1

LCM = int((no1 * no2)/GCD)

print("LCM of", no1 , " and ", no2, " is ", LCM)
print("GCD of", no1 , " and ", no2, " is ", GCD)

'''Output of Pragram16

Enter number 115
Enter number 23
LCM of 15  and  3  is  15
GCD of 15  and  3  is  3 '''
