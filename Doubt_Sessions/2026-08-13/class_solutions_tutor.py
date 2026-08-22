# '''
# ## Question 1: Personal Expense Analyzer

# ### Use Case
# An economics student wants to analyse weekly personal expenses.

# ### What You Have to Do
# Create a function `calculate_expenses(expenses)` that:
# 1. Accepts a list of expenses.
# 2. Calculates total expense.
# 3. Calculates average expense.
# 4. Finds highest and lowest expense.
# 5. Returns all four results.

# ### Sample Input
# ```text
# 250
# 400
# 150
# 300
# 500
# ```

# ### Sample Output
# ```text
# Total Expense = 1600
# Average Expense = 320.0
# Highest Expense = 500
# Lowest Expense = 150
# ```


# '''
# def calculate_expenses(expenses):
#     total=sum(expenses)
#     average = total/ len(expenses)
#     highest = max(expenses)
#     lowest = min(expenses)
#     return total, average, highest, lowest


# expenses = []
# for i in range(3):
#     amount = float(input(f"Enter your expense {i+1}= "))
#     expenses.append(amount)

# # print(expenses)
# # print(calculate_expenses(expenses))
# total, average, highest, lowest = calculate_expenses(expenses)

# print(f"The sum of the expenses is {total}")
# print(f"The average of the expenses is {average}")
# print(f"The highest expense is {highest}")
# print(f"The lowest expense is {lowest}")


# def salary_analyzer(employee_info):
#     total_salary = 0
#     highest_name = ""
#     highest_salary = 0
#     lowest_name = ""
#     lowest_salary = 0
#     above_50000=0

#     first_employee = True
    
#     for name,salary in employee_info.items():
#         total_salary += salary

#         if salary > 50000:
#             above_50000+=1

#         if first_employee:
#             highest_name = name
#             highest_salary = salary

#             lowest_name = name
#             lowest_salary = salary

#             first_employee = False
#         else :
#             if salary > highest_salary:
#                 highest_salary = salary
#                 highest_name = name

#             if salary < lowest_salary:
#                 lowest_salary = salary
#                 lowest_name = name

#     average_salary = total_salary/len(employee_info)

#     return [average_salary, highest_name, highest_salary, lowest_name, lowest_salary, above_50000]


# employees_info={
#     "Aanya": 45000,
#     "Ishaan": 60000,
#     "Rohit": 55000,
#     "Seema": 75000,
#     "Prabhanjan": 40000
# }

# results = salary_analyzer(employees_info)
# print(f"Average Salary = {results[0]}\nHighest Salary is for {results[1]} and it is {results[2]}")

'''
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

def analyze_sales(sales_data):
    company_total = 0
    highest_region=""
    highest_regions_sales=0
    product_totals={}

    for region,products in sales_data.items():
        region_total=0
        for product,sales in products.items():
            region_total += sales
            company_total+=sales
            if product in product_totals:
                product_totals[product]+=sales
            else:
                product_totals[product]=sales
        if region_total>highest_regions_sales:
            highest_regions_sales=region_total
            highest_region=region
    highest_product = ""
    highest_product_sales=0
    for product, sales in  product_totals.items():
        if sales>highest_product_sales:
            highest_product_sales=sales
            highest_product=product

    return [company_total, highest_region,highest_product, highest_product_sales]
sales_data = {
    "Pune":{
        "Laptop": 50000,
        "Phone": 30000,
        "Tablet": 20000
    },
    "Mumbai":{
        "Laptop": 70000,
        "Phone": 45000,
        "Tablet": 25000
    }
}

print("Regional Sales")
result = analyze_sales(sales_data)

print(f"Total Company Sales = {result[0]}")
print(f"Highest Sales Region = {result[1]}")
print(f"Highest Selling Product = {result[2]} : {result[3]}")