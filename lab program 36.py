#Program 36
#Write a program to create a dictionary of product name and price. Return
#the price of the product entered by the user.
#Name: Neha Namburi
#Date of Excetution: October 14, 2020
#Class: 11

d={} # empty dict
ans='y'

while((ans=='y') or (ans=='Y')):
    # values of p and pr are local to this while loop- i.e. once leaves loop, new values
    p=input("enter product name")
    pr=float(input("enter price"))
    d[p]= pr
    ans= input("enter y or Y to continue")

print(d)

p=input("enter product name")
for i in d:
    if(i==p):
        print("price =", d[i])
        break

else:
    print("product not found")

        
''' Output for Program 36

enter product nameapple
enter price200
enter y or Y to continuey
enter product namebanana
enter price250
enter y or Y to continuey
enter product nameorange
enter price140
enter y or Y to continuej
{'apple': 200.0, 'banana': 250.0, 'orange': 140.0}
enter priduct nameorange
price = 140.0
'''
