# Python Assignment 04 – Functions & Nested Collections

## Doubt Session Assignment



---

# 🟢 EASY

## Question 1: Personal Expense Analyzer

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
```



---

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



---

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
```



---

# 🟡 MEDIUM

## Question 4: Student Result Management System

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
```


---

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



---

## Question 6: Employee Salary Dictionary

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



---

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
```



---

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



---

## Question 9: Student Attendance & Performance System

### Use Case
A college wants to analyse attendance and marks together.

### Data Structure
```python
students = {
    "Rahul": {"attendance": 85, "marks": 78},
    "Priya": {"attendance": 92, "marks": 88}
}
```

### What You Have to Do
Create `analyze_students(students)` that:
- Iterates through every student.
- Checks eligibility: attendance >= 75%.
- Checks result: marks >= 40.
- Displays each student's status.
- Counts eligible, ineligible, passed and failed students.

### Sample Output
```text
Rahul
Attendance = 85%
Marks = 78
Attendance Status = Eligible
Result = Pass

Priya
Attendance = 92%
Marks = 88
Attendance Status = Eligible
Result = Pass

Summary
Eligible Students = 2
Ineligible Students = 0
Passed Students = 2
Failed Students = 0
```



---

## Question 10: Mini Business Inventory & Sales System

### Use Case
A small business wants one program to manage products, prices, stock and sales.

### Initial Data
```python
products = {
    "Rice": {"price": 60, "stock": 20},
    "Sugar": {"price": 45, "stock": 15},
    "Oil": {"price": 120, "stock": 10}
}
```

### What You Have to Do

Create separate functions for:

#### 1. Display Inventory
Display product name, price and stock.

#### 2. Sell Product
Accept product name and quantity.
- Check whether product exists.
- Check whether sufficient stock exists.
- Calculate bill.
- Reduce stock.
- Return bill amount.

#### 3. Add Product
Accept product name, price and stock and add it to the dictionary.

#### 4. Remove Product
Remove an existing product.

#### 5. Inventory Summary
Display:
- Total number of products.
- Total units available.
- Highest-priced product.
- Lowest-priced product.
- Total inventory value.

### Sample Input
```text
Sell Product: Rice
Quantity: 5

Add Product: Wheat
Price: 50
Stock: 25
```

### Sample Output
```text
Sale Successful
Product = Rice
Quantity = 5
Total Bill = 300

Product Added Successfully
Product = Wheat
Price = 50
Stock = 25

Inventory Summary
Total Products = 4
Total Units = 60
Highest Priced Product = Oil
Lowest Priced Product = Sugar
```



---

# Final Revision Checklist

- [ ] Variables
- [ ] Input/output
- [ ] Type casting
- [ ] Arithmetic operators
- [ ] Comparison operators
- [ ] Logical operators
- [ ] If-else
- [ ] For loops
- [ ] While loops
- [ ] Nested loops
- [ ] Lists
- [ ] Tuples
- [ ] Sets
- [ ] Dictionaries
- [ ] Nested collections
- [ ] Collection methods
- [ ] Functions
- [ ] Parameters
- [ ] Return values
- [ ] Functions with collections
- [ ] Functions with nested collections

## Goal

For every problem, first identify:
1. What data do I have?
2. Which data structure is appropriate?
3. Do I need a loop?
4. Do I need a nested loop?
5. What should the function receive?
6. What should the function return?
7. What conditions need to be checked?

Then write the Python program.
