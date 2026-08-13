#q01
# inventory = [{"name": "rice", "price": 80}, {"name": "dal", "price": 120}]
# print(inventory[1]["name"])#dal
# print(inventory[0]["price"])#80

# #q02
# names = ["rice", "dal", "sugar"]
# prices = [80, 120]
# print(dict(zip(names, prices))) #{'rice': 80, 'dal': 120}

# # #q03
# inventory = [
#     {"name": "rice", 
#      "price": 80,
#     "stock": 12},
#     {"name": "dal", 
#      "price": 120, 
#      "stock": 5},
#     {"name": "soap", 
#      "price": 30, 
#      "stock": 40},
# ]

# print(inventory[0]["name"])   
# print(inventory[2]["stock"])  
# inventory[1]["stock"] -= 1
# print(inventory[1]["stock"])  

# #q04
# shelf = ["rice", "dal", "sugar"]
# for pos, name in enumerate(shelf, start=1):
#   print(pos, name)

# names=["tea", "biscuits"]
# prices = [250, 30]
# fuse= dict(zip(names,prices))
# print(fuse)

# #q05
# sales = ["snacks", "grains", "snacks", "soap", "snacks", "grains"]
# counts = {}
# for cat in sales:
#   counts[cat] = counts.get(cat, 0) + 1
# print(counts)
# products = [
#     {"name": "rice", "price": 80},
#     {"name": "ghee", "price": 550},
#     {"name": "sugar", "price": 42},
# ]
# by_price = sorted(products, key=lambda x: x["price"], reverse=True)
# print(by_price[0]["name"], by_price[0]["price"])

#q06
