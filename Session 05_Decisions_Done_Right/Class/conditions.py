'''
condition statments - This statements are used to execute a particular block of code based on the conditions
types:
1. If block
    Syntax:
    if condition:
        
2. if-else block
3. if-elif-else block
4. nested if, or nested if-else or nested if-elif-else


else is not mandatory it is always optional
elif is abbreviation of else if
if yiou are using else you should strictly bind it with if or elif you cannot just use else. 
we can write conditions only in if and elif else do not have any condition
'''

# bill_amount = int(input("Enter your total bill amount = "))

# if bill_amount >=500 :
#     print("Eligible for discount")
#     print("The discounted amount is ",(0.2*bill_amount))
# elif bill_amount>=300 : 
#     print("The discounted amount is ",(0.1*bill_amount))
# else:
#     print(f"You are not eligible for discount. Please shop for {500-bill_amount} rs. more")

# print("Happy Shopping")

# nested if-else

# print("Welcome to MSRTC")

# gender = input("Enter you gender = ")#MaLe, MAle, 
# age = int(input("Enter your age = "))

'''
if you are male
    exempted - youra ge is above 75 or equal or you age is less than or equal to 4
    full fare

if you are female
    exempted - your age is above 75 or your age is less than or equal to 4
    50% - all womens

'''

# if gender.lower() == 'male':
#     if age>=75 or age<=4:
#         print("you have free ticket")
#     else : 
#         print("You have full ticket")
# elif gender.lower() == 'female' :
#     if age>=75 or age<=4:
#         print("you have free ticket")
#     else : 
#         print("You have half ticket")
# else :
#     print("Enter a valid gender")

# if condition:
#     print()
# else:
#     print()

num1 = int(input("Enter a number = "))
num2 = int(input("Enter a number = "))

'''
shorthand if 
syntax - if condition : statement
'''

# if num1>num2 : print(f"{num1} is greater than {num2}")#30>30(false)

'''
shorthand if-else
syntax - 
print() if (condition) else print()
print() before if is executed when the condition is true and if it is false the print after else is executed
'''

# print(f" output is from shorthand if-else {num1} is greater than {num2}") if num1>num2 else print(f"output is from shorthand if-else{num2} is greater than {num1}")


# print(f" {num1} is greater than {num2}") if num1>num2 else print(f"{num1} is equal to {num2}") if num1==num2 else print(f"{num2} is greater than {num1}")

'''
if num1>num:
    condint
else:
    if num1==num2:
        condt
    else:
'''
'''
pass - we use this to initialse blank if or else
'''

if num1>num2:
    pass
elif num1<num2:
    pass
else:
    print("nothign worked")