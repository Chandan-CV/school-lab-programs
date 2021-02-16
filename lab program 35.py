#Program 35
#Write a program to count frequency of elements using dictionary
#Name: lithika ramesh
#Date of Excetution: September 30, 2020
#Class: 11

d={}
s='Python is a very interesting language, phython is very interesting'
l=s.split()
for w in l:
    if w not in d:
        c=l.count(w)
        d[w]=c

print(d)

''' Outout for program 35
{'Python': 1, 'is': 2, 'a': 1, 'very': 2, 'interesting': 2, 'language,': 1, 'phython': 1}

'''




