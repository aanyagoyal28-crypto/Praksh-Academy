import sqlite3
connection=sqlite3.connect("store.db")
cursor=connection.cursor()

# cursor.execute(
#     '''
# CREATE TABLE IF NOT EXISTS Customers(
# customer_id INTEGER PRIMARY KEY,
# name TEXT,
# city TEXT
# )
# '''
# )

# cursor.execute(
#     '''
# CREATE TABLE IF NOT EXISTS Orders(
# order_id INTEGER PRIMARY KEY,
# customer_id INTEGER,
# product TEXT,
# category TEXT,
# quantity INTEGER,
# price REAL
# )
# '''
# )
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS orders_new(
#     order_id INTEGER PRIMARY KEY, 
#     customer_id INTEGER, 
#     product TEXT,
#     category TEXT, 
#     quantity INTEGER, 
#     price REAL
# )
# ''')

cursor.execute(
    '''SELECT * from orders
    '''
    )
for row in cursor.fetchall():
    print(row)
customers = [
    (1, "Aanya", "Muscat"),
    (2, "Ishaan", "Muscat"),
    (3, "Prabhanjan", "Pune"),
    (4, "Vishal", "Pune"),
    (5, "Brinda", "Gujarat"),
    (6, "Saranya","Pune")
]

cursor.executemany(
    '''INSERT INTO Customers(customer_id,name, city)
    VALUES(?, ?, ?) 
    ''',customers
)

orders = [
    (101, 1, "Laptop", "Electronics", 1, 60000),
    (102, 1, "Mouse", "Electronics", 2, 800),
    (103, 2, "Keyboard", "Electronics", 1, 1500),
    (104, 3, "Chair", "Furniture", 2, 5000),
    (105, 3, "Desk", "Furniture", 1, 10000),
    (106, 4, "Laptop", "Electronics", 1, 60000),
    (107, 5, "Chair", "Furniture", 1, 5000)
]

# cursor.executemany(
#     ''' INSERT INTO Orders(order_id, customer_id, product, category, quantity, price)
#     VALUES(?,?,?,?,?,?)
# ''',orders
# )
cursor.executemany("""
INSERT INTO orders_new
(order_id, customer_id, product, category, quantity, price)
VALUES (?, ?, ?, ?, ?, ?)
""", orders)

# cursor.execute(
#     '''SELECT name,city from Customers
#     WHERE city='Muscat'
#     '''
    # )
# cursor.execute(
#    '''
#      SELECT * from orders_new
#      WHERE price> 50000
#      '''
# )
# for row in cursor.fetchall():
#     print(row)

# cursor.execute(
#     '''
# Select* from Customers
# ''')
# for row in cursor.fetchall():
#     print(row)
# cursor.execute(
#     '''
# Select* from orders_new 
# ''')

# for row in cursor.fetchall():
#     print(row)

cursor.execute("""
SELECT
c.name,
o.product,
o.order_id
FROM customers c
LEFT JOIN orders_new o
on c.customer_id= o.customer_id
WHERE c.city='Pune' 
""")

for row in cursor.fetchall():
    print(row)