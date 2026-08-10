marks_of_students=[590,458,578,367,600]

# def calculate_percentage(scored_marks):
#     percentage = scored_marks/6
#     return percentage

# result = map(calculate_percentage,marks_of_students)
# print(list(result))
#syntax : map(function/lambda function, arguments)

percentage = list(map(lambda scored_marks : scored_marks/6, marks_of_students))
print(percentage)