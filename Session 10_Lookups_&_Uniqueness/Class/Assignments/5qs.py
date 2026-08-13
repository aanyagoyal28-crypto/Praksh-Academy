#q1p
prices = {
    "eggs": 120,
    "bread": 80,
    "dal": 45,
    "rice": 60,
    "sugar": 50
}
print(prices)
prices["dal"]+=10
prices.pop("rice")
print(prices)

#q2
prices = {
    "eggs": 120,
    "bread": 80,
    "dal": 45,
    "rice": 60,
    "sugar": 50
}
if "bread" in prices:
    print(prices["bread"])
else:
    print("Not stocked")

#q3
cart = {
    "dal": 1,
    "tea": 2, 
    "soap": 4
    }
