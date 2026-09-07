import pandas as pd
khata= pd.DataFrame({"product":["Maggi","MAGGI","parle-g","Tata-Salt",None,"Maggi"],
    "qty":[5,5,10,None,2,5],
    "amount":["70","70","100","84","eighty","70"]
    })
print(khata)

print("Missing values: ")
print(khata.isna())

print("Missing value count: ")
print(khata.isna().sum())

drop_data= khata.dropna()
print(drop_data)

fill_data= khata.copy()

fill_data= fill_data.fillna({
    "qty": 0,
    "product" : "unknown"
})
print(fill_data)

print("Duplicated rows: ")
print(khata.duplicated())

print("Duplicated rows count: ")
print(khata.duplicated().sum())

no_duplicates=khata.drop_duplicates()
print(no_duplicates)

standard_data= khata.copy()
standard_data["product"]= standard_data["product"].str.lower().str.strip()
print(standard_data)