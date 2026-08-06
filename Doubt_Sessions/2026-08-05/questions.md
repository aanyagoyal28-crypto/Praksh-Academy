## 📚 Topics Covered

This assignment is designed to revise all the concepts covered so far.

### Previously Covered Concepts

- Variables
- Input & Output
- Type Casting
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- if-else
- for Loop
- while Loop
- Nested for Loop
- Nested while Loop

### New Concepts

- List
- Tuple
- Set
- Dictionary
- Iteration on Data Structures
- List Methods
- Tuple Methods
- Set Methods
- Dictionary Methods

---

# 🎯 Learning Objectives

After completing this assignment, the student should be able to:

- Create and use Lists, Tuples, Sets and Dictionaries.
- Iterate through every data structure.
- Perform insertion, deletion and update operations.
- Apply loops with collections.
- Solve real-world business and economics problems.
- Build logical thinking using Python.

---

# 📋 Instructions

- Read every question carefully.
- Use meaningful variable names.
- Display outputs neatly.
- Use loops wherever required.
- Do not use concepts that are not taught yet (Functions, Classes, etc.)

---

# 🟢 EASY LEVEL

---

# Question 1: Shopping Cart Manager (List)

## 🛒 Real World Scenario

A supermarket wants to build a small shopping cart application. Whenever a customer shops, the products should be stored inside a shopping cart.

Your task is to create a simple shopping cart using a Python List.

---

## Problem Statement

Write a Python program that:

- Accepts **5 product names** from the user.
- Stores all the products inside a List.
- Displays the complete shopping cart.
- Ask the user to enter one more product.
- Add the product to the cart.
- Ask the user for one product they want to remove.
- Remove that product from the list.
- Display the final shopping cart.

---


---

## Sample Input

```text
Enter Product 1 : Rice
Enter Product 2 : Wheat
Enter Product 3 : Sugar
Enter Product 4 : Milk
Enter Product 5 : Bread

Enter product to add :
Butter

Enter product to remove :
Sugar
```

## Sample Output

```text
Initial Shopping Cart

Rice
Wheat
Sugar
Milk
Bread

Updated Shopping Cart

Rice
Wheat
Milk
Bread
Butter
```

---

## Explanation

Initially, the shopping cart contains five products.

The customer later adds Butter and removes Sugar.

The final list should contain the updated products.

---

# Question 2 : Monthly Sales Analysis (Tuple)

## 💰 Real World Scenario

A company stores monthly sales data. Since previous month's sales should never be modified, they are stored inside a Tuple.

---

## Problem Statement

Write a Python program that:

- Store sales of six months inside a Tuple.
- Display all the sales values.
- Find the highest sale.
- Find the lowest sale.
- Calculate the average sales.
- Find how many times a particular sales value occurs using count().
- Find the index of a given sales value using index().

---



---

## Sample Input

```text
Sales

25000
28000
32000
28000
35000
40000

Enter value to search

28000
```

## Sample Output

```text
Sales Data

25000
28000
32000
28000
35000
40000

Highest Sales : 40000

Lowest Sales : 25000

Average Sales : 31333.33

28000 occurred 2 times

First occurrence at Index 1
```

---

## Explanation

A Tuple cannot be modified.

The student only needs to analyse the data.

---

# Question 3 : Unique Customer Cities (Set)

## 🌍 Real World Scenario

An online shopping company stores customer cities.

Many customers may belong to the same city.

Instead of storing duplicates, they decide to use a Set.

---

## Problem Statement

Write a Python program that:

- Accept 8 city names.
- Store them inside a Set.
- Display all unique cities.
- Ask the user to add one more city.
- Remove one city.
- Display the updated Set.
- Display the total number of unique cities.

---



---

## Sample Input

```text
Pune
Mumbai
Delhi
Pune
Nagpur
Mumbai
Nashik
Kolhapur

Add City

Satara

Remove City

Delhi
```

## Sample Output

```text
Unique Cities

Pune
Mumbai
Nagpur
Nashik
Kolhapur

Satara

Total Unique Cities : 6
```

---

## Explanation

Since Set stores only unique values,

Pune and Mumbai are stored only once.


---

# 🟡 MEDIUM LEVEL

---

# Question 4: Student Information System (Dictionary)

## 🎓 Real World Scenario

A college wants to store information about a student in a structured format. Since every piece of information has a key (such as Name, Age, Course, etc.), a **Dictionary** is the perfect choice.

---

## Problem Statement

Write a Python program that:

- Create an empty dictionary.
- Accept the following details from the user:
  - Student Name
  - Age
  - Course
  - City
  - Percentage
- Store all the details in the dictionary.
- Display all the student details using a loop.
- Update the student's percentage.
- Remove the city from the dictionary.
- Display the updated dictionary.

---



---

## Sample Input

```text
Student Name : Rahul
Age : 20
Course : Economics
City : Pune
Percentage : 82

Updated Percentage : 87
```

## Sample Output

```text
Student Details

Name : Rahul
Age : 20
Course : Economics
City : Pune
Percentage : 82

Updated Student Details

Name : Rahul
Age : 20
Course : Economics
Percentage : 87
```

---

## Explanation

The dictionary stores student information using **key-value pairs**.

After updating the percentage and removing the city, the updated dictionary is displayed.

---

# Question 5: Daily Expense Tracker (List + Loops)

## 💵 Real World Scenario

An economics student wants to track daily expenses during a week.

Instead of calculating everything manually, create a Python program to analyse the expenses.

---

## Problem Statement

Write a Python program that:

- Accept daily expenses until the user enters **-1**.
- Store every expense inside a List.
- Display all expenses.
- Calculate:
  - Total Expense
  - Average Expense
  - Highest Expense
  - Lowest Expense
- Sort the list in ascending order.
- Display the sorted list.


---

## Sample Input

```text
120
350
450
200
600
-1
```

## Sample Output

```text
Expenses

120
350
450
200
600

Total Expense : 1720

Average Expense : 344.0

Highest Expense : 600

Lowest Expense : 120

Sorted Expenses

120
200
350
450
600
```

---

## Explanation

The program keeps accepting expenses until **-1** is entered.

The value **-1** is not stored in the list.

---

# Question 6: Product Inventory Manager (Dictionary)

## 🏪 Real World Scenario

A shop owner wants to maintain the quantity of products available in the store.

Each product has a unique name and its quantity.

A Dictionary is the best data structure for this task.

---

## Problem Statement

Write a Python program that:

- Create a dictionary containing the following products:

```text
Rice : 40
Sugar : 25
Milk : 30
Bread : 20
```

- Display all products and quantities.
- Ask the user for a product name.
- Update its quantity.
- Ask the user for another product.
- Remove that product from the dictionary.
- Display the updated inventory.
- Display the total number of products remaining.

---



---

## Sample Input

```text
Product to Update

Milk

New Quantity

45

Product to Remove

Sugar
```

## Sample Output

```text
Current Inventory

Rice : 40
Sugar : 25
Milk : 30
Bread : 20

Updated Inventory

Rice : 40
Milk : 45
Bread : 20

Total Products = 3
```

---

## Explanation

The dictionary is first displayed.

The quantity of **Milk** is updated.

Finally, **Sugar** is removed from the inventory and the updated dictionary is displayed.

---

---

# 🟡 MEDIUM LEVEL

---

# Question 4: Student Information System (Dictionary)

## 🎓 Real World Scenario

A college wants to store information about a student in a structured format. Since every piece of information has a key (such as Name, Age, Course, etc.), a **Dictionary** is the perfect choice.

---

## Problem Statement

Write a Python program that:

- Create an empty dictionary.
- Accept the following details from the user:
  - Student Name
  - Age
  - Course
  - City
  - Percentage
- Store all the details in the dictionary.
- Display all the student details using a loop.
- Update the student's percentage.
- Remove the city from the dictionary.
- Display the updated dictionary.

---



---

## Sample Input

```text
Student Name : Rahul
Age : 20
Course : Economics
City : Pune
Percentage : 82

Updated Percentage : 87
```

## Sample Output

```text
Student Details

Name : Rahul
Age : 20
Course : Economics
City : Pune
Percentage : 82

Updated Student Details

Name : Rahul
Age : 20
Course : Economics
Percentage : 87
```

---

## Explanation

The dictionary stores student information using **key-value pairs**.

After updating the percentage and removing the city, the updated dictionary is displayed.

---

# Question 5: Daily Expense Tracker (List + Loops)

## 💵 Real World Scenario

An economics student wants to track daily expenses during a week.

Instead of calculating everything manually, create a Python program to analyse the expenses.

---

## Problem Statement

Write a Python program that:

- Accept daily expenses until the user enters **-1**.
- Store every expense inside a List.
- Display all expenses.
- Calculate:
  - Total Expense
  - Average Expense
  - Highest Expense
  - Lowest Expense
- Sort the list in ascending order.
- Display the sorted list.

---


---

## Sample Input

```text
120
350
450
200
600
-1
```

## Sample Output

```text
Expenses

120
350
450
200
600

Total Expense : 1720

Average Expense : 344.0

Highest Expense : 600

Lowest Expense : 120

Sorted Expenses

120
200
350
450
600
```

---

## Explanation

The program keeps accepting expenses until **-1** is entered.

The value **-1** is not stored in the list.

---

# Question 6: Product Inventory Manager (Dictionary)

## 🏪 Real World Scenario

A shop owner wants to maintain the quantity of products available in the store.

Each product has a unique name and its quantity.

A Dictionary is the best data structure for this task.

---

## Problem Statement

Write a Python program that:

- Create a dictionary containing the following products:

```text
Rice : 40
Sugar : 25
Milk : 30
Bread : 20
```

- Display all products and quantities.
- Ask the user for a product name.
- Update its quantity.
- Ask the user for another product.
- Remove that product from the dictionary.
- Display the updated inventory.
- Display the total number of products remaining.

---



---

## Sample Input

```text
Product to Update

Milk

New Quantity

45

Product to Remove

Sugar
```

## Sample Output

```text
Current Inventory

Rice : 40
Sugar : 25
Milk : 30
Bread : 20

Updated Inventory

Rice : 40
Milk : 45
Bread : 20

Total Products = 3
```

---

## Explanation

The dictionary is first displayed.

The quantity of **Milk** is updated.

Finally, **Sugar** is removed from the inventory and the updated dictionary is displayed.

---


---

# 🔴 CHALLENGE LEVEL

---

# Question 7: Employee Salary Statistics (Tuple)

## 💼 Real World Scenario

An HR department wants to analyze employee salaries. Since salary records should not be modified accidentally, they are stored in a **Tuple**.

The HR manager wants a report showing important statistics about the salaries.

---

## Problem Statement

Write a Python program that:

- Store the salaries of **8 employees** inside a Tuple.
- Display all salaries.
- Calculate:
  - Highest Salary
  - Lowest Salary
  - Average Salary
- Ask the user to enter a salary value.
- Display:
  - Number of times the salary appears.
  - Index of its first occurrence.
- Display all salaries greater than ₹50,000.

---



---

## Sample Input

```text
25000
40000
55000
60000
45000
70000
55000
80000

Search Salary

55000
```

---

## Sample Output

```text
Employee Salaries

25000
40000
55000
60000
45000
70000
55000
80000

Highest Salary : 80000

Lowest Salary : 25000

Average Salary : 53750.0

55000 appears 2 times.

First occurrence at Index 2.

Employees earning more than ₹50000

55000
60000
70000
55000
80000
```

---

## Explanation

The tuple stores fixed salary data.

The student must analyze the tuple using built-in methods and iteration.

---

# Question 8: Movie Ticket Booking System (Nested List)

## 🎬 Real World Scenario

A cinema has **3 rows** with **4 seats** in each row.

Each seat stores the name of the customer who booked it.

The manager wants to display the seating arrangement.

---

## Problem Statement

Write a Python program that:

- Create a Nested List having **3 rows and 4 columns**.
- Accept customer names for every seat.
- Display the seating arrangement in a tabular format.
- Ask the user for a customer name.
- Check whether the customer has booked a seat.
- Display the row number where the customer is sitting.

---



---

## Sample Input

```text
Rahul
Priya
Amit
Neha

Rohan
Aakash
Sneha
Ritu

Vikas
Pooja
Manoj
Kiran

Search Customer

Sneha
```

---

## Sample Output

```text
Movie Hall Seating

Rahul Priya Amit Neha

Rohan Aakash Sneha Ritu

Vikas Pooja Manoj Kiran

Sneha found in Row 2.
```

---

## Explanation

Each inner list represents one row of seats.

The student must use **nested loops** to display and search the seating arrangement.

---

# Question 9: Word Frequency Counter (Dictionary)

## 📚 Real World Scenario

A publishing company wants to know how many times every word appears in an article.

Instead of counting manually, build a Python program that calculates the frequency of each word.

---

## Problem Statement

Write a Python program that:

- Accept a sentence from the user.
- Split the sentence into individual words.
- Create a Dictionary where:
  - Key = Word
  - Value = Number of occurrences
- Display the dictionary.
- Display:
  - Total Unique Words
  - Most Frequently Occurring Word
- Ask the user for a word.
- Display how many times it occurs.

---



---

## Sample Input

```text
python is easy and python is powerful

Search Word

python
```

---

## Sample Output

```text
Word Frequency

python : 2

is : 2

easy : 1

and : 1

powerful : 1

Total Unique Words : 5

Search Result

python occurs 2 times.
```

---

## Explanation

The program creates a dictionary dynamically by counting every word in the sentence.

The `get()` method can be used to simplify the counting process.

---

---

# Question 10: Mini Library Management System
## 📚 (Lists + Sets + Dictionaries + Loops)

### 🔴 Difficulty Level
**Challenge**

---

## 📖 Real World Scenario

A college library wants to build a small system to keep track of books issued to students.

The librarian wants to:

- Maintain a list of all books available.
- Maintain a set of registered students (to avoid duplicate registrations).
- Maintain a dictionary showing which student has borrowed which book.

Your task is to create a simple Library Management System using the concepts learned so far.

---

## 📝 Problem Statement

Write a Python program that performs the following tasks:

### Step 1

Create a List containing the following books.

```text
Python Basics
Economics 101
Statistics
Business Mathematics
Data Science
```

---

### Step 2

Create an empty Set to store registered students.

Accept **5 student names** from the user.

Store them inside the Set.

Display all registered students.

---

### Step 3

Create an empty Dictionary.

Ask the user to assign one book to every registered student.

Store the data in the following format.

```text
Student Name : Book Name
```

Example

```text
Rahul : Python Basics

Priya : Statistics
```

---

### Step 4

Display the complete Library Record.

---

### Step 5

Ask the librarian to enter the name of a student.

Display the book borrowed by that student.

If the student is not found,

display

```text
Student Not Found
```

---

### Step 6

Ask the librarian to enter a student name whose book has been returned.

Remove that student from the Dictionary.

Display the updated Library Record.

---

### Step 7

Display the following information.

- Total Books Available
- Total Registered Students
- Total Books Currently Issued

---

## 💡 Hint

You may use the following methods.

### List

- append()
- remove()
- len()

### Set

- add()
- remove()

### Dictionary

- get()
- pop()
- items()
- keys()
- values()

---

## 🎯 Concepts Covered

- List
- Set
- Dictionary
- for loop
- while loop
- if-else
- Dictionary Iteration
- Set Iteration
- List Iteration
- Membership Operator (`in`)
- get()
- pop()
- len()

---

## ⌨️ Sample Input

```text
Registered Students

Rahul
Priya
Amit
Sneha
Rohit

Book Allocation

Rahul
Python Basics

Priya
Statistics

Amit
Economics 101

Sneha
Business Mathematics

Rohit
Data Science

Search Student

Priya

Return Book

Rahul
```

---

## 🖥️ Sample Output

```text
Registered Students

Rahul
Priya
Amit
Sneha
Rohit

Library Record

Rahul -> Python Basics

Priya -> Statistics

Amit -> Economics 101

Sneha -> Business Mathematics

Rohit -> Data Science

Search Result

Priya has borrowed Statistics

Updated Library Record

Priya -> Statistics

Amit -> Economics 101

Sneha -> Business Mathematics

Rohit -> Data Science

Summary

Total Books Available : 5

Registered Students : 5

Books Issued : 4
```

---

## 📖 Explanation

The program uses three different data structures.

- **List** stores all books.
- **Set** stores unique student names.
- **Dictionary** stores which student borrowed which book.

The program demonstrates how different Python collections work together in a real-world application.

---

# ⭐ Bonus Challenge (Optional)

Create a **Student Result Management System** that stores:

- Student Name
- Marks of 5 Subjects
- Percentage
- Grade
- Pass/Fail Status

Use:

- Dictionary
- List
- Loops
- if-else

Display the final report in a neat tabular format.

---
