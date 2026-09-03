     
import sqlite3
connection = sqlite3.connect('store.db')
cursor = connection.cursor()


cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS products(
        PRODUCT_ID TEXT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        PRICE REAL NOT NULL,
        STOCK INTEGER NOT NULL,
        CATEGORY TEXT NOT NULL,
        PRODUCT_TYPE TEXT NOT NULL
        )
    '''
)
cursor.execute("INSERT INTO products (PRODUCT_ID, NAME, PRICE, STOCK, CATEGORY, PRODUCT_TYPE) VALUES('P101', 'Rice', 60, 20, 'Food', 'Regular')")
cursor.execute("INSERT INTO products (PRODUCT_ID, NAME, PRICE, STOCK, CATEGORY, PRODUCT_TYPE) VALUES('P102', 'Milk', 40, 20, 'Food', 'Perishable')")
cursor.execute("INSERT INTO products (PRODUCT_ID, NAME, PRICE, STOCK, CATEGORY, PRODUCT_TYPE) VALUES('P103', 'Laptop', 120000, 10, 'Electronics', 'Regular')")
cursor.execute("INSERT INTO products (PRODUCT_ID, NAME, PRICE, STOCK, CATEGORY, PRODUCT_TYPE) VALUES('P104', 'Notebook', 70, 100, 'Stationery', 'Regular')")

cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

for row in rows:
    print(row)


connection.commit()
connection.close()

