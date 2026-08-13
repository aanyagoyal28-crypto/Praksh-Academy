'''## Question 1: Personal Expense Analyzer

### Use Case
An economics student wants to analyse weekly personal expenses.

### What You Have to Do
Create a function `calculate_expenses(expenses)` that:
1. Accepts a list of expenses.
2. Calculates total expense.
3. Calculates average expense.
4. Finds highest and lowest expense.
5. Returns all four results.

### Sample Input
```text
250
400
150
300
500
```

### Sample Output
```text
Total Expense = 1600
Average Expense = 320.0
Highest Expense = 500
Lowest Expense = 150
'''

# def calculate_expenses (expenses):
#     total= sum(expenses)
#     average = total/len(expenses)
#     highest= max(expenses)
#     lowest = min(expenses)
#     return total, average, highest, lowest




# expenses=[]
# for i in range(5):
#     amount= float(input(f'Enter the amount {i+1} : '))
#     expenses.append(amount)

# print(expenses)

# total, average, highest , lowest = calculate_expenses(expenses)

# print(f"Total Expenses = {total}")
# print(f"Average Expense = {average}")
# print(f"Highest Expense = {highest}")
# print(f"Lowest Expenses = {lowest}")


'''
## Question 2: Product Price Manager

### Use Case
A store wants to apply a discount to all product prices.

### What You Have to Do
Create `apply_discount(prices, discount_percentage)` that:
- Accepts a list of prices.
- Applies the discount to every price.
- Stores the results in a new list.
- Returns the new list.

### Sample Input
```text
1000
500
2500
800

Discount = 10
```

### Sample Output
```text
Original Prices:
1000
500
2500
800

Discounted Prices:
900.0
450.0
2250.0
720.0
```

'''

def apply_discount(prices , discount_percentage=0.1):
   new_prices=[i-(i*discount_percentage) for i in prices]
   print(new_prices)

1
    




prices=[]
for i in range(4):
    amount= float(input(f"Enter the price {i+1} = "))
    prices.append(amount)

print(prices)


apply_discount(prices)