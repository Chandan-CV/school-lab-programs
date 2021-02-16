#Program 17
#Write a program to input some numbers repeatedly and print  their sum.
#The program ends when the user says no more to enter (normal termination)
#or program ends when the number entered is less than zero
#Name : Adeesh Devanand
#Date of Execution: August 10, 2020
#Class 11

count = ssum = 0
ans = 'y'
while(ans == 'y'):
    n = int(input("Enter the no"))
    if(n<0):
        print("Aborting")
        break
    ssum += n
    count += 1
    ans = input("Enter y or n")
else:
    print("You have entered", count, 'nos')
print("Sum of numbers =", ssum)

''' Output of Program17

Enter the no5
Enter y or ny
Enter the no6
Enter y or ny
Enter the no-5
Aborting
Sum of numbers = 11  '''
