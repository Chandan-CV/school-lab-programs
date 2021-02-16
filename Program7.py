#Program 7
#Write a program to accept name, roll no, class of a student. Accept marks of 4 subject
#subjects of this student(on 100). Calculate Total, Average and Percentage and display
#in marks card template
#Name : Adeesh Devanand
#Date of Execution: July 17, 2020
#Class 11

name = str(input("Enter name of the student"))
roll = str(input("Enter roll no of the student"))
c = str(input("Enter class of the student"))

m1 = float(input("enter marks of subject 1"))
m2 = float(input("enter marks of subject 2"))
m3 = float(input("enter marks of subject 3"))
m4 = float(input("enter marks of subject 4"))

total = m1 + m2 + m3 + m4
Average = total/ 4
Percentage = Average

print("Name of student", name)
print("Roll no of student", roll)
print("Class of student", c)

print("Marks in Subject 1", m1)
print("Marks in Subject 2", m2)
print("Marks in Subject 3", m3)
print("Marks in Subject 4", m4)

print("Total = ", total,"\nAverage = ", Average,"\nPercentage = ", Percentage)

'''Output of Program 7

Enter name of the studentAdeesh
Enter roll no of the student1
Enter class of the student11
enter marks of subject 1100
enter marks of subject 290
enter marks of subject 395
enter marks of subject 489
Name of student Adeesh
Roll no of student 1
Class of student 11
Marks in Subject 1 100.0
Marks in Subject 2 90.0
Marks in Subject 3 95.0
Marks in Subject 4 89.0
Total =  374.0 
Average =  93.5 
Percentage =  93.5 '''
