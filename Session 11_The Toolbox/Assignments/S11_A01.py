# #q01
# def apply_discount(bill):
#  return bill * 0.90
# print(apply_discount(1200))#1080.0
# print(apply_discount(560))#504.0

# #q02
# def add(a, b):
#  print(a + b)
# result = add(40, 25)
# print(result)

# #q03
# def bill_line(item, qty, price):
#     return f"{item} x{qty} = Rs {qty * price}"

# print(bill_line("Rice", 2, 80))
# print(bill_line("Soap", 3, 35))


# #q04
# def greet(name, lang="en"):
#     if lang == "hi":
#         return f"Namaste, {name}!"
#     else:
#         return f"Hello, {name}!"

# print(greet("Sunita"))
# print(greet("Sunita", lang="hi"))
# print(greet(lang="hi", name="Ramesh"))

# #q05
# def split_bill(bill):
#     gst = round(bill * 0.05, 2)
#     total = round(bill + gst, 2)
#     return bill, gst, total
# amount, gst, total = split_bill(400)
# print(amount, gst, total)

# #q06
# def apply_discount(bill, rate=0.10):
#    return round(bill * (1 - rate), 2)
# print(apply_discount(1200))
# print(apply_discount(1200, rate=0.15))

# #q07
# def bill_line(item, qty, price):
#  return f"{item} x{qty} = Rs {qty * price}"
# print(bill_line("Rice", 2 , 80)) # only 

#q08
def bill_line(item, qty, price):
    return f"{item} x{qty} = Rs {qty * price}"
def apply_discount(bill, rate=0.10):
    return(round(bill * (1-rate),2))
def add_gst(amount):
    return(round(amount* 1.05,2 ))
print(bill_line("Rice", 2, 80))
print(bill_line("Oil", 1, 150))
subtotal = 2*80 + 1*150
print(f"Subtotal: Rs {subtotal}")
discounted = apply_discount(subtotal)
to_pay = add_gst(discounted)
print(f"To pay: Rs {to_pay}")

#q09-doubt
def is_low_stock(qty, level=5):
    return qty<level
def stock_summary(stock):
    low=0
    ok=0
    if is_low_stock(qty):
        print(f"{name}: {qty} (LOW)")
        low += 1
    else:
        print(f"{name}: {qty} (ok)")
        ok += 1
    return low, ok
stock = {"rice": 12, "dal": 3, "soap": 40, "salt": 2}




# #q10
# add_gst = lambda p: round(p * 1.05, 2)
# print(add_gst(100))
# result = list(map(add_gst, [40, 60, 200]))
# print(result)