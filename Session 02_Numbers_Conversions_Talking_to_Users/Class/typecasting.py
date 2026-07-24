'''
typecasting -> When we convert a variables datatype into the required format. 
int, float, str, bool are the most common datatypes used in python.
10(int) -> 10.00(float)(data loss not present)
10.20(float) -> 10(int)(data loss not present)

syntax : 
int(variable_name) -> converts the variable into integer datatype
float(variable_name) -> converts the variable into float datatype
str(variable_name) -> converts the variable into string datatype
'''

num1 = 10
print(type(num1))#int
# you have to convert num1 to float and string

num1_float=float(num1)
print(type(num1_float))#float

num1_str=str(num1)
print(type(num1_str))#str


