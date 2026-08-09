'''
1. input of 5 itesm whcih user want's to add in list.

var1 = input1
var2 = input2
.
.
.
list and add all variable
'''
purchaser_cart = []
for i in range(5):
    item = input("Enter item to add in cart: ")
    purchaser_cart.append(item)
print(purchaser_cart)
