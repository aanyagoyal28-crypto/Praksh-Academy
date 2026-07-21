'''
Rules:
1. Variables can be alphanumerical(A-Z, a-z, 0-1) and can include underscores (_).
2. Variables cannot start with a number.
3. Variables cannot be a reserved keyword in Python.(class, if, def, return, else, etc.)
4. Variables are case-sensitive. For example, myVariable and myvariable are two different variables.
5. Variables should be defined in snake case format. For example, my_variable is a valid variable name.(Snake case format means that words are separated by underscores and all letters are in lowercase.)
6. Variables should be descriptive and meaningful. For example, instead of using a variable name like x or y, use a name that describes the purpose of the variable, such as student_name or total_score.

'''
name='Prabhanjan'
Name='Rushi'
print(name)
print(Name)
print(10)
print(name, 'Bhosale')
print("Good Evening", name)

_name='Aanya'
print(_name)

name_1='Rohit'
print(name_1)

# if = 20 - invalid using predefined keyword.

a=10
b=20
c=30

a=b=c=30 #dynamic assignment
print(a,b,c)
a,b,c=10,20,30 #multiple assignment

print(a,b,c)