#Program 26
#Write a program to print TRUE if all the elements in tuple1 are in tuple2
#Name : Adeesh Devanand
#Date of Execution: September 21, 2020
#Class 11

t1 = tuple(input())
t2 = (1, 2, 4, 'a', 12, 'b' ,'d', ' ')
check = True
for x in t1:
    if x not in t2:
        check = False
        break
print(check)

'''Output of Program26
a b
True
'''
