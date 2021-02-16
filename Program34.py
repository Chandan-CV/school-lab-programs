#Program 34
#Create a dictionary of product name and price.
#Return the price of product entered by the user
#Name : Adeesh Devanand
#Date of Execution: October 14, 2020
#Class 11

d = {}
ans = 'y'
while ans == 'y' or ans == 'Y':
    p = input("Enter the product").lower()
    price = float(input("Enter the price"))
    d[p] = price
    ans = input("Enter y or Y to continue entering")
print(d)

p = input("Enter product name").lower()
if p in d:
    print("Price of the product", p, "is", d[p])
else:
    print("Product not present")
'''Output of Program34
Enter the productCheese
Enter the price2
Enter y or Y to continue enteringy
Enter the productButter
Enter the price3
Enter y or Y to continue enteringy
Enter the productButter
Enter the price35
Enter y or Y to continue enteringn
{'cheese': 2.0, 'butter': 35.0}
Enter product nameBUTTer
Price of the product butter is 35.0
'''
