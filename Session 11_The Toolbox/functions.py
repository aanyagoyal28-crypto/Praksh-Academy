'''
functions - this helps us to reuse a particular block of code. 
syntax : 

def function_name(arguments)
def - keyword
function_name is nothting but a variable to define the name
arguments - values passed to function to process and generate result. 

1. paramaterized add(1,2)
2. non-paramaterized add()

functins are of mainly 4 types
1. parameterzied return function
2. parameterzied non-return function
3. non-parameterized return function.
4. non-parameterized non return function.
'''

#parameterzied return function
# def add(num1,num2):
#    print(num1+num2)

# solution = add(5,10)
# print(solution)

# def add():
#     num1 = int(input("Enter a = "))
#     num2 = int(input("Enter b = "))
#     return num1+num2

# print(add())
'''
formal arguments - this are the argumetns which are used while defining a function
actual argumnts - this ae the arumets which are used while caling the functions

'''

# def check_rules(a=0,b=0):
#     print("Value of a is ",a)
#     print("Value of b is ",b)

# check_rules(4,5)
# check_rules(5)

# def normal_sentence(name, city,country):
#     print("My name is ",name)
#     print("I belong to ",city)
#     print("I'm from ",country)

# normal_sentence("Prabhanjan",city = "Pune",country = "India")
'''
If. you are using mixed that is positional and keyword argumens the postitinal should ge at first then keywords
'''

'''
*args - if ou don't know how many number of arguments neededto pass. 
'''

# def students(*std):
#     for i in std:
#         print(i)

# students_list=["Raj","Rajat"]

# students(students_list)

#scope

a=0
b=0
def add(a,b):
    print(a+b)
    print(a)
    print(b)

add(5,10)
print(a)
print(b)