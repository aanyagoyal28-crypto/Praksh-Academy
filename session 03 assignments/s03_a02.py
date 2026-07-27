shop = "PRAKSH MART"
print(shop[0]) #P
print(shop[-1]) # T
print(len(shop)) #11

#q2
shop = "PRAKSH MART"
print(shop[:6]) # PRAKSH
print(shop[7:11]) # MART
print(shop[::-1]) # reverse

#q3
item = "sugar-1KG"
name = item[:5]
weight = item[6:]
print(name)
print(weight)

#q4
raw = " MAGGI noodles "
clean = raw.strip().title()
print(clean)
print(clean.upper())
print("sugar-1KG".replace("-", " "))

#q5
shop = "PRAKSH MART"
print("MART" in shop)
print(shop.find("MART"))
print(shop.count("A"))


#q6
stock = "rice,dal,sugar,salt"
print(stock.split(","))
print(len(stock.split(",")))

#Q7
shop = "praksh mart"
change= shop.upper()
print(change)

#Q8
raw = " RICE-basmati-5KG "
clean = raw.strip().split("-")
print(clean)
final= raw.strip().title()
print(final)

#Q9
record = "PM1023:Sugar 1kg:42"
code= record[:6]
Name = record[7:16]
price = record[17:]
print ("Code:" ,code)
print("Name:" , Name)
print ("Price: Rs" , price)
print("Reversed code:", code[::-1])
print("Starts with PM?", code[:2] == "PM")

#q10
offers = ["Rice 5% off", "Free candy above Rs 500"]
print(" | ".join(offers))

price = 12.5
print(f"Rs {price:.2f}")
