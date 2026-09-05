import requests

response= requests.get(
    "https://dummyjson.com/products"
)

print(response.status_code)

data= response.json()
print(data)

import sqlite3
connection = sqlite3.connect('restaurant.db')
cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS products(
customer_id INTEGER,
product TEXT,
 category TEXT,
quantity INTEGER,
price REAL
)
""")
connection.commit()
connection.close()






# products= data["products"]
# print(products)
# print(products[0]["title"])
# print(products[0]["price"])

# for product in products:
#     print(product["title"], product["price"], product["dimensions"]["width"])
