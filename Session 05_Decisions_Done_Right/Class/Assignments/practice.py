#q01
bill = int (input ( "Enter bill amount:")) 
if bill > 500:
    print ("Discount Unlocked!")

#q02
packets= 10 
if packets < 5:
    print ("Restock needed")
else:
    print ("Stock OK")

#q03
bill = 800
if bill > 500:
    discount = 0.05
    print("5% discount")
elif bill > 1000:
    discount = 0.10
    print("10% discount")

bill = 800
if bill > 1000:
    discount = 0.10
    print("10% discount")
elif bill > 500:
    discount = 0.05
    print("5% discount")  # doesn't print same output for 1200 as it is greater than 1000 and the first true will print 

#q04
bill = int(input("Enter bill amount: "))

if bill > 1000:
    discount = 0.10
elif bill > 500:
    discount = 0.05
else:
    discount = 0

saved = bill - bill * discount
print(f"Final payable amount: {saved:.2f}")

#q05
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
if total > 1000:
    discount = 0.10
elif total > 500:
    discount = 0.05
else:
    discount = 0

saved = total * discount
final = total - saved

print(f"{'DISCOUNT':<22}{saved:>8.2f}")
print(f"{'TO PAY':<22}{final:>8.2f}")


if total > 1000 and is_member == True:
    print(f"{'FREE HOME DELIVERY':^30}")

    






