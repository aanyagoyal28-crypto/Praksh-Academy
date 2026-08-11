#q01
double = lambda x: x * 2
print(double(21)) #42
print(double(100))#200

#q02
prices = [40, 60]
result = map(lambda p: p * 2, prices)
print(list(result)) #[80, 120]

#q03
prices = [40, 60, 80, 200]

result = list(map(lambda p: round(p * 1.05, 2), prices))
print(result)

#q04
stock = [("Rice", 40), ("Soap", 3), ("Oil", 12), ("Salt", 2)]
result=list(filter(lambda p: p[1]<5,stock))
print(result)

#q05
prices = [40, 60, 80]
double= list(map(lambda x: x * 2, prices))
print(double)
double_comp = [p * 2 for p in prices]
print(double_comp)
filtered= list(filter(lambda p : p>50 , prices))
print(filtered)
filtered_comp=[p for p in prices if p>50]
print(filtered_comp)

#q06
def factorial(n):
    if n == 0:         
        return 1
    return n * factorial(n - 1)

def sum_to(n):
    if n == 0:         
        return 0
    return n + sum_to(n - 1)

print(factorial(5))
print(sum_to(10))

#q07
prices = [40, 60, 80]
doubled = list(map(lambda p: p * 2, prices))#without typecasting to list, it is only object
print(len(doubled))
print(doubled)

#q08
bills = [("Sunita", 620), ("Ramesh", 180), ("Meera", 940), ("Ayaan", 500)]
winners=list(filter(lambda p : p[1]>500, bills))
print("Coupon Winners")
for name, price in winners:
    print(f"{name} - Rs {price}")
mapped = list(map(lambda p: f"{p[0]}: Rs {p[1]}", bills))
print(mapped)

#q09(DOUBT)


#q10
import math
print(math.ceil(47.2))
from datetime import date
print(date(2026, 7, 15).strftime("%d-%m-%Y"))
