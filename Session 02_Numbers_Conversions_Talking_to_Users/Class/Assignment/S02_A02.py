#q1
print(100 - 20 * 2) #60
print((100 - 20) * 2) #160
print(10 / 2)#5.0

#q2
print(17 // 5) #3
print(17 % 5) #2
print("3" * 2) #string operation is allowed but correct answer won't print
print(3*2)

#q3
int(4.9)
int(-2.7)
int("20") + 5
float("4.5")
str(250) + " rupees" #typecasting as int pushes the number towards 0 instead of rounding.
print (int(4.9))
print (int(-2.7))
print (int("20") + 5)
print (float("4.5"))
print (str(250) + " rupees")


#q4
money=100
biscuits_cp = 8
print (money // biscuits_cp)
print (money % biscuits_cp)
print (2**10)

#q5
stock = 4
is_regular = True
bill = 620

print (stock < 10)
print (stock == 0)
print (is_regular ==True and bill > 500)
print (bill >1000 or is_regular== True)
print (is_regular == False)


#q6
total = 0
#add sugar 
total+= 42
#add rice
total+= 58
#rs 10 festval copoun 
total-=10
print (total)
print (f"Total: {total}")

#q7
price = "185"
delivery = 15
print (int(price) +delivery)

#q8
product = "Sugar"
qty = 3
price = 42.5
paid = 200
print(f"3 x sugar = {qty*price}")
print(f"Change to return = {paid-(qty*price)}")

#q9
bill=1745
print (f"Rs 500 x {bill//500}")
bill= bill % 500
print (f"Rs 100 x {bill//100}")
bill= bill % 100
print (f"Rs 20 x {bill//20}")
bill= bill % 20
print (f"Rs 5 x {bill//5}")
