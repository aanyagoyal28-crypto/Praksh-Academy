'''
Basic data operations: 
1. Check missing values
2. Drop missing values
3. Fill missing values
4. Find duplicates
5. Drop duplicates
6. Standardise text
7. Assign cleaned text back
8. Convert amount to numeric
9. Handle missing amount
10. Create a cleaning pipeline
11. Apply
12. GroupBy
13. GroupBy + Agg
14. GroupBy + Merge
15. Concat
16. Pivot Tables
17. Categoty * Month Pivot
18. Final Answer

'''
import pandas as pd
khata = pd.DataFrame({
    "product":["Maggi","MAGGI","parle-g","Tata-Salt",None,"Maggi"],
    "qty":[5,5,10,None,2,5],
    "amount":["70","70","100","84","eighty","70"]
})
# print(khata)
#staging_data = khata.copy()
print("Missing Values : ")
print(khata.isna())

print("Missing Values Count :",khata.isna().sum())

drop_data = khata.dropna()
print(khata)
print(drop_data)

fill_data = khata.copy()

fill_data = fill_data.fillna({
    "qty":0,
    "product":"Unknown"
})

print(fill_data)

print("Duplicated rows: ")
print(khata.duplicated())

print("Duplicated rows count: ")
print(khata.duplicated().sum())


no_duplicates = khata.drop_duplicates()
print(no_duplicates)


clean_products = khata["product"].str.lower().str.strip()
print(clean_products)
'''
staging_data = []

'''

clean_khata = khata.copy()
clean_khata["product"] = clean_khata["product"].str.lower().str.strip()
print(clean_khata)

print("Original dataype ",khata["amount"].dtype)

clean_khata['amount'] = pd.to_numeric(
clean_khata['amount'], errors='coerce'
)

print("After   conversion ",clean_khata["amount"].dtype)

average_amount = clean_khata["amount"].mean()
clean_khata["amount"]= clean_khata["amount"].fillna(average_amount)

'''
cleaning pipeline
'''

clean_khata = khata.copy()

# Step 1: Standardise product names
clean_khata["product"] = (
    clean_khata["product"]
    .str.strip()
    .str.lower()
)

# Step 2: Convert amount to numeric
clean_khata["amount"] = pd.to_numeric(
    clean_khata["amount"],
    errors="coerce"
)

# Step 3: Fill missing product names
clean_khata["product"] = clean_khata["product"].fillna(
    "unknown"
)

# Step 4: Fill missing quantity
clean_khata["qty"] = clean_khata["qty"].fillna(0)

# Step 5: Fill missing amount
clean_khata["amount"] = clean_khata["amount"].fillna(
    clean_khata["amount"].mean()
)

# Step 6: Remove duplicates
clean_khata = clean_khata.drop_duplicates()

print(clean_khata)
