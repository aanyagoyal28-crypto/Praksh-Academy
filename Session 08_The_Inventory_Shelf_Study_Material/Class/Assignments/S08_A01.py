#q1
products = ["rice", "dal", "sugar", "oil", "soap"]
print(products[0]) #rice
print(products[-1]) #soap
print(products[1:3]) #dal, sugar
#q2
prices = [55, 20, 80]
print(prices.sort()) #ascending order
print(prices)
#q3
products =["rice", "dal", "sugar", "oil", "soap", "tea"]
print(products[0])
print(products[-1]) 
print(products[2:4])
print(len(products))
#q4
stock = ["rice", "dal"]
stock.append("sugar")
stock.insert(1, "oil")
stock.extend(["soap", "tea"])
print(stock)
prices = [80, 120, 42]
prices[2] = 45
print(prices)
#q5
items = ["rice", "dal", "sugar", "dal"]
items.count ("dal")
print(items.count("dal"))
items.remove("dal")
print(items)
print(items.pop())
print(items)
print(items.index("sugar"))
print("rice" in items)
#q6
prices = [55, 20, 80, 45]
new_prices= sorted(prices)
print(new_prices)
print(prices)
print(sorted(new_prices, reverse=True))
#q7
# prices = [55, 20, 80]
# prices = prices.sort()
# print(prices)#no list selected
prices = [55, 20, 80]
print(prices.sort()) 
print(prices)
#q8
products = ["rice", "dal", "sugar"]
prices = [80, 120, 42]
products.append("oil"), prices.append(160)
products.extend(["soap", "tea"]), prices.extend([35, 55])
prices[2]= 45
print(f"Products: {products}")
print(f"Prices: {prices}")
print(f"Total items: {len(products)}")
print(f"Cheapest first: {sorted(prices)}")
#q9
hours = (9, 21)
open_hr, close_hr = hours
print(f"Open for {close_hr - open_hr} hours")
gst_rates = (0, 5, 12, 18, 28)
print(f"GST slabs: {gst_rates}")
print(f"Standard slab: {gst_rates[2]}")
daily_sales = [450, 120, 890, 300, 675]
print(f"Top 3: {sorted(daily_sales, reverse=True)[:3]}")
print(f"Original safe: {daily_sales}")

a, b = "Rice", "Dal"
a, b = b, a
print(f"Swapped: {a}, {b}")

#q10
# Dictionary
price_book = {
    "rice": 80,
    "dal": 120,
    "sugar": 45}
print(price_book['dal'])
customers = ["asha", "ravi", "asha", "meena", "ravi"]
unique_customers = set(customers)
print(f"{len(unique_customers)} unique customers")