'''
Lambda function is a small anonymous function
lambda function can take any number of arguments but will have only on expression

syntax:
lambda arguments: expression
'''

# def calculate_percentage(scored_marks):
#     percentage = scored_marks/6
#     return percentage

# scored = int(input("Enter your marks = "))
# # percentage = calculate_percentage(scored)
# percentage = lambda scored_marks : scored_marks/6
# print(f"Your percentage is ",percentage(scored))

num = int(input("Enter a number = "))
power = int(input("Enter power of a number = "))

result = lambda num,power : num ** power

print(result(num,power))