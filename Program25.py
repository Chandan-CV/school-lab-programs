#Program 25
#Write a program to print a tuple ('a', 'bb', 'ccc'.....'zz..24 times')
#Name : Adeesh Devanand
#Date of Execution: September 21, 2020
#Class 11

l = []
for x in range(97, 123):
    l.append(chr(x)* (x -96))
t = tuple(l)
print(t)

'''Output of Program25
('a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg', 'hhhhhhhh',
'iiiiiiiii', 'jjjjjjjjjj', 'kkkkkkkkkkk', 'llllllllllll', 'mmmmmmmmmmmmm',
'nnnnnnnnnnnnnn', 'ooooooooooooooo', 'pppppppppppppppp', 'qqqqqqqqqqqqqqqqq',
'rrrrrrrrrrrrrrrrrr', 'sssssssssssssssssss', 'tttttttttttttttttttt',
'uuuuuuuuuuuuuuuuuuuuu', 'vvvvvvvvvvvvvvvvvvvvvv',
'wwwwwwwwwwwwwwwwwwwwwww','xxxxxxxxxxxxxxxxxxxxxxxx',
'yyyyyyyyyyyyyyyyyyyyyyyyy', 'zzzzzzzzzzzzzzzzzzzzzzzzzz')'''
