
#q1
print(f"{12.5:.2f}") #12.50
print(f"{1250000:,}") #1,250,000
print(f"{0.157:.1%}") # 15.7%

#q2
print(f"{'Maggi':<10}|")
print(f"{'Maggi':>10}|")
print(f"{'Maggi':^10}|")

#q3
sales = 1250000
price = 7.5
growth = 0.157
print(f"{sales:,}")
print(f"{price:.2f}")
print(f"{growth:.1%}")
print(f"{sales:,.2f}")


#q4
print(f"{'PRAKSH MART':*^40}")
print(f"{'Rice 5kg':<15}{320.00:.2f}")
print(f"{'Maggi':<15}{14.00:.2f}")

#q5
items = ["rice", "dal", "sugar"]
print(", ".join(items))
print(" | ".join(items))

#q6
code = "PM1023"
print(code.startswith("PM"))
print(code[2:].isdigit())
print("Maggi".isalpha())
print("12.50".isdigit())  

#q7
price = 42.5
print(f"Rs {price:>8.2f}")

#q8
line = "-" * 30
print(f"{'PRAKSH MART':^30}")
print(line)
print(f"{'ITEM':<18}{'QTY':>4}{'PRICE':>8}")
print(line)
print(f"{'Rice 5kg':<18}{1:>4}{320.00:>8.2f}")
print(f"{'Maggi Noodles':<18}{3:>4}{42.00:>8.2f}")
print(f"{'Sugar 1kg':<18}{2:>4}{89.00:>8.2f}")
print(line)
total = 320.00 + 42.00 + 89.00
print(f"{'TOTAL':<22}{total:>8.2f}")
print(line)

#q9
line = "-" * 30
print (f"{'SUBTOTAL':<22}{451.00:>8.2f}")
GST= 451.00*0.05
print(f"{'GST@5%':<22}{GST:>8.2f}")
print(line)
print(f"{'GRAND TOTAL':<22}{GST+451.00:>8.2f}")
        


#q10
bill = 650
if bill > 500:
    print("5% off unlocked")
    print(f"You pay: Rs {bill * 0.95:.2f}")
