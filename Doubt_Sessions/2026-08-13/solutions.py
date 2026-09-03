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

# def apply_discount(prices , discount_percentage=0.1):
#    new_prices=[i-(i*discount_percentage) for i in prices]
#    print(new_prices)

# 1
    




# prices=[]
# for i in range(4):
#     amount= float(input(f"Enter the price {i+1} = "))
#     prices.append(amount)

# print(prices)


# apply_discount(prices)

'''
## Question 3: Unique Customer Analysis

### Use Case
An online business collects customer cities, but many customers may belong to the same city.

### What You Have to Do
Create `analyze_cities(cities)` that:
- Converts the list to a set.
- Removes duplicates.
- Returns the unique cities.
- Displays the number of unique cities.

### Sample Input
```text
Pune
Mumbai
Pune
Delhi
Mumbai
Nashik
```

### Sample Output
```text
Unique Cities:
Pune
Mumbai
Delhi
Nashik

Total Unique Cities = 4


'''

# def anaylse_cities(cities):
#     unique_cities=set(cities)
#     return unique_cities

# cities=[]
# for i in range(5):
#     city= input("Enter a city name : ")
#     cities.append(city)
# print(cities)

# unique_cities= anaylse_cities(cities)


# print("Unique cities:")
# for c in unique_cities:
#  print (c)

# print(f"Total unique cities = {len(unique_cities)}")


'''
Student Result Management System

### Use Case
A college wants to automatically calculate student results.

### What You Have to Do
Create `calculate_result(marks)` that:
- Accepts a list of marks.
- Calculates total and average.
- Returns Pass if average is at least 40, otherwise Fail.

### Sample Input
```text
75
82
68
55
70
```

### Sample Output
```text
Total Marks = 350
Average Marks = 70.0
Result = Pass
'''

# def calculate_result(marks):
#     total = sum(marks)
#     average = total / len(marks)
#     if average >= 40:
#         result = "Pass"
#     else:
#         result = "Fail"
#     return total, average, result


# marks = []
# for i in range(5):
#     mark = int(input("Enter the marks : "))
#     marks.append(mark)

# print(marks)

# total, average, result = calculate_result(marks)
# print(f"Total: {total}")
# print(f"Average: {average:.2f}")
# print(f"Result: {result}")


'''

## Question 5: Bank Transaction Analyzer

### Use Case
A bank stores deposits as positive numbers and withdrawals as negative numbers.

### What You Have to Do
Create `analyze_transactions(transactions)` that calculates:
- Total deposits
- Total withdrawals
- Number of deposits
- Number of withdrawals
- Final balance

### Sample Input
```text
5000
-1500
2500
-500
3000
-1000
```

### Sample Output
```text
Total Deposits = 10500
Total Withdrawals = 3000
Number of Deposits = 3
Number of Withdrawals = 3
Final Balance = 7500


```




'''
# def analyse_transactions(transactions):
#     deposits=0
#     withdrawals=0
#     count_deposits=0
#     count_withdrawals=0
#     for i in transactions:
#         if i>0:
#             deposits+=i
#             count_deposits+=1
#         else:
#             withdrawals+=i
#             count_withdrawals+=1
#     final_balance = deposits+withdrawals
#     return [deposits, withdrawals, count_deposits, count_withdrawals, final_balance]

# transactions= [5000,-1500,2500,-500,3000,-1000]
# result= analyse_transactions(transactions)
# print(result)
# print(f"Analysis Results\n Total Deposits= {result[0]}\n Total Withdrawals = {result[1]}\n Count of Deposits = {result[2]}\n Count of Withdrawals = {result[3]}\n Final Balance = {result[4]}")

'''
# Question 6: Employee Salary Dictionary

### Use Case
A company stores employee names and salaries in a dictionary and wants salary statistics.

### What You Have to Do
Create `salary_analysis(employees)` that:
- Calculates average salary.
- Finds highest-paid employee.
- Finds lowest-paid employee.
- Counts employees earning more than ₹50,000.
- Returns the results.

### Sample Input
```text
Rahul : 45000
Priya : 60000
Amit : 55000
Sneha : 75000
Rohan : 40000
```

### Sample Output
```text
Average Salary = 55000.0
Highest Salary = Sneha : 75000
Lowest Salary = Rohan : 40000
Employees earning above 50000 = 3
```


'''

# def salary_analysis(employees):
#     average_salary=0
#     highest_salary=0
#     highest_name= ""
#     lowest_salary=0
#     lowest_name=""
#     above_50000=0
#     total_salary=0

#     first_employee= True

#     for name, salary in employees.items():
#         total_salary+=salary

#         if salary>50000:
#          above_50000+=1

#         if first_employee:
#             highest_salary= salary
#             highest_name = name

#             lowest_salary= salary
#             lowest_name=name
#             first_employee= False
#         else:
#            if salary>highest_salary:
#               highest_salary=salary
#               highest_name= name
#            if salary< lowest_salary:
#               lowest_salary=salary
#               lowest_name= name

#     average_salary= total_salary/len(employees)
#     return [average_salary,highest_salary, highest_name, lowest_salary, lowest_name, above_50000]

# employees={
#    "Aanya" :45000,
#    "Ishaan" : 600000,
#    "Rohit": 55000,
#    "Seema" : 70000,
#    "Prabhanjan": 45000,
# }

# result= salary_analysis(employees)
# print(result)


'''
## Question 7: Monthly Economic Data Analyzer

### Use Case
An economics student stores monthly inflation rates in a tuple because the observations should remain unchanged.

### What You Have to Do
Create `analyze_inflation(rates)` that:
- Calculates average inflation.
- Finds highest and lowest inflation.
- Counts months with inflation above 5%.
- Returns the analysis.

### Sample Input
```text
4.2
5.1
6.3
4.8
5.7
6.0
```

### Sample Output
```text
Average Inflation = 5.35
Highest Inflation = 6.3
Lowest Inflation = 4.2
Months Above 5% = 4

# '''
# def analyze_inflation(rates):
#     total = 0
#     above_5 = 0
#     first_rate = True
#     for rate in rates:
#         total += rate
#         if rate > 5.0:
#             above_5 += 1
#         if first_rate:
#             highest_inflation = rate
#             lowest_inflation = rate
#             first_rate = False
#         else:
#             if rate > highest_inflation:
#                 highest_inflation = rate
#             if rate < lowest_inflation:
#                 lowest_inflation = rate

#     average = total / len(rates)

#     return average, highest_inflation, lowest_inflation, above_5


# rates = (4.2, 5.1, 6.3, 4.8, 5.7, 6.0)

# average, highest_inflation, lowest_inflation, above_5 = analyze_inflation(rates)

# print(f"Average Inflation = {round(average, 2)}")
# print(f"Highest Inflation = {highest_inflation}")
# print(f"Lowest Inflation = {lowest_inflation}")
# print(f"Months Above 5% = {above_5}")

'''

# 🔴 CHALLENGE

## Question 8: Regional Sales Analyzer

### Use Case
A company operates in multiple regions. Each region has sales for several products.

### Data Structure
```python
{
    "Pune": {"Laptop": 50000, "Phone": 30000, "Tablet": 20000},
    "Mumbai": {"Laptop": 70000, "Phone": 45000, "Tablet": 25000}
}
```

### What You Have to Do
Create functions that:
- Calculate total sales for each region.
- Calculate total company sales.
- Find the region with highest sales.
- Find the product with highest overall sales.
- Use nested loops.

### Sample Output
```text
Regional Sales

Pune = 100000
Mumbai = 140000

Total Company Sales = 240000
Highest Sales Region = Mumbai
```
'''
def sales_analyzer(sales):
  company_total=0
  highest_region_sales=0
  highest_region_name=""
  products_total={}
  for city, product in sales.items():
    region_total=0
    for item, price in product.items():
     print(city, item, price)
     region_total+=price
     company_total+=price
     if item in products_total:
       products_total[item]+=price
     else:
       products_total[item]=price
    if region_total> highest_region_sales:
      highest_region_sales= region_total
      highest_region_name = city
  highest_product=""
  highest_product_sales=0
  for item,price in products_total.items():
    if price>highest_product_sales:
      highest_product_sales=price
      highest_product=item

  return[company_total,highest_region_sales,highest_region_name,highest_product, highest_product_sales]


   
sales = {
    "Pune": {"Laptop": 50000, "Phone": 30000, "Tablet": 20000},
    "Mumbai": {"Laptop": 70000, "Phone": 45000, "Tablet": 25000}
}

result= sales_analyzer(sales)

print("Sales Analysis:")
# print(f"Total Company Sales = {result[0]}")