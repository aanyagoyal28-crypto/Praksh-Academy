#q1
products=("milk" , "bread" , "eggs, butter, cheese, coffee")
print(products[0])
print(products[-1])
print (products[2:4])
print(len(products))
#q2
prices = [80, 120, 42]
prices.append(65)
prices.extend([30, 55])
prices[2]= 45
print(prices)
#q3
daily_sales = [450, 120, 890, 300, 675]
sorted_sales = sorted(daily_sales , reverse=True)
print(sorted_sales)
print(sorted_sales[0:3])
#q4
rices = [80, 120, 42]
prices.append(65)
prices.extend([30, 55])
prices[2] = 45
print(prices)

#q5

print(sorted(daily_sales, reverse=True)[:3])
print(daily_sales)
