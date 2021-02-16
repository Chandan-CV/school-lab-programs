#Program 33
#Write a program to count frequency of elements of list using dictionaries
#Name : Adeesh Devanand
#Date of Execution: September 23, 2020
#Class 11

d = {}
s = 'Python is a very easy language Python is interesting'
l = s.split()
for w in l:
    if w not in d:
        c = l.count(w)
        d[w] = c
print(d)
'''Output Of Program33
{'Python': 2, 'is': 2, 'a': 1, 'very': 1,
'easy': 1,'language': 1, 'interesting': 1}
'''
