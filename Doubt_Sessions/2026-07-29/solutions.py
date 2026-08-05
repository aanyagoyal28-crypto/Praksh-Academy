'''# Assignment 1: Student Percentage & Pass/Fail

## Question
Write a program that asks the user to enter marks of **5 subjects** (each out of 100).

Your program should:
1. Calculate the total marks.
2. Calculate the percentage.
3. Print **Pass** if the percentage is **40 or above**, otherwise print **Fail**.
4. Display the results neatly.

### Sample Input
```
English: 70
Maths: 80
Science: 65
History: 60
Computer: 90
```

### Sample Output
```
Total Marks = 365
Percentage = 73.0%
Result = Pass
```
'''
# english = int(input("English : "))
# maths = int(input("Maths : "))
# science = int(input("Science: "))
# history = int(input("History :"))
# computer = int(input("Computer : "))

# total = english + maths + science + history + computer 
# print(f"Total Marks = {total}")
# percentage = total/5
# print(f"Percentage = {percentage} %")
# if percentage >= 40:
#     print("Result = Pass")
# else:
#     print("Result = Fail")

'''# Assignment 2: Even/Odd & Divisibility

## Question
Take a number from the user.

Your program should:
1. Check whether it is even or odd.
2. Check whether it is divisible by both **3 and 5**.

### Sample Input
```
30
```

### Sample Output
```
The number is Even.
The number is divisible by both 3 and 5.
```

---'''
# number = int(input("Enter a number :"))
# if number==0:
#     print("The number is neither")
# elif number%2==0:
#     print("The number is Even")
# else:
#     print("The number is Odd")

# if number%3==0 and number%5==0:
#     print("The number is divisible by both 3 and 5")
# else:
#     print("The number is not divisible by both 3 and 5")
'''# Assignment 3: Arithmetic Operations

## Question
Take two numbers from the user and display:
- Addition
- Subtraction
- Multiplication
- Division (/)
- Floor Division (//)
- Modulus (%)

Also print whether the first number is greater than the second.

### Sample Input
```
20
6
```

### Sample Output
```
Addition = 26
Subtraction = 14
Multiplication = 120
Division = 3.3333333333333335
Floor Division = 3
Remainder = 2
First number is greater.

'''
'''# Assignment 4: Salary Bonus Calculator

## Question
Ask the user to enter their salary.

Rules:
- Salary > 50000 → Bonus = 20%
- Salary between 30000 and 50000 → Bonus = 10%
- Otherwise → Bonus = 5%

Print the bonus amount and final salary.

### Sample Input
```
45000
```

### Sample Output
```
Bonus = 4500.0
Final Salary = 49500.0
```
'''
# salary = int(input("Enter your salary : "))
# if salary > 50000:
#     bonus=0.2
# elif salary > 30000:
#     bonus=0.1
# else:
#     bonus=0.5
# bonus_paid = salary*bonus 
# final_salary= salary + bonus_paid
# print(f"Bonus = {bonus_paid:.1f}")
# print (f"Final Salary = {final_salary:.1f}")

'''# Assignment 6: Login System

## Question
Store the following credentials:

```
Username: admin
Password: python123
```

Ask the user to enter both values.

If both are correct, print:
```
Login Successful
```

Otherwise print:
```
Invalid Credentials
```
'''
# username = "admin"
# password = "python123"
# input_username= input("Enter your username : ")
# input_password = input("Enter your password : ")

# if input_username.lower()==username and password== input_password :
#     print("Login Successful")
# else:
#     print("Invalid Credentials")



'''
# Assignment 8: Largest of Three Numbers

## Question
Take three numbers from the user.

Find and display the largest number using only if-elif-else statements.

### Sample Input
```
15
42
28
```

### Sample Output
```
Largest = 42'''

num1= int(input("Enter a number : "))
num2= int(input("Enter a number : "))
num3= int(input("Enter a number : 1"))

if num1>num2 and num1>num3:
    print(f"Largest = {num1}")
elif num2>num1 and num2>num3:
    print(f"Largest = {num2}")
else:
    print(f"Largest = {num3}")