# students_data = [
#     ['Aanya',98,90,87],
#     ['Prabhanjan',99,90,88],
#     ['Siddharth',100,90,89]
# ]

# print(students_data)
# print(students_data[0][0])#['Aanya', 98, 90, 87]
# print(students_data[2][3])


# for students in students_data:
#     print("name = ",students[0])
#     total = 0
#     # for marks in students[1:]:
#     #     total +=marks
#     marks = students[1:]#marks[98, 90, 87]
#     total = sum(marks)
#     print("Total marks = ",total)


# students_data ={
#     "Stud_001":{
#         "Name": "Aanya",
#         "Age": 17,
#         "Country": "Oman"
#     },
#     "Stud_002":{
#         "Name": "Prabhanjan",
#         "Age": 18,
#         "Country": "India"
#     },
#     "Stud_003":{
#         "Name": "Siddharth",
#         "Age": 19,
#         "Country": "USA"
#     }
# }

# print(students_data.values())
# print(students_data['Stud_001']['Age'])
# print(students_data.items())
'''
(
    'Stud_001', 
    {
        'Name': 'Aanya', 
        'Age': 17, 
        'Country': 'Oman'
    }
)


'''
# for student_id, student_info in students_data.items():
#     print("Student ID = ", student_id)
#     print("Name = ", student_info['Name'])
#     print("Age = ", student_info['Age'])
#     print("Country = ", student_info['Country'])
#     print("-------------------")

# for students in students_data.keys():
#     print(students)


books=[
    {
        "Title": "The Great Gatsby",
        "Author": "F. Scott Fitzgerald",
        "Year": 1925
    },
    {
        "Title": "To Kill a Mockingbird",
        "Author": "Harper Lee",
        "Year": 1960
    },
    {
        "Title": "1984",
        "Author": "George Orwell",
        "Year": 1949
    }
]

print(len(books))

for item in books:
    print(item)
    print("Title = ", item['Title'])
    print("Author = ", item['Author'])
    print("Year = ", item['Year'])
    print("-------------------")


#"Enumerate"

'''
How to choose the correct data type
Structure       Ordered     changeable     Duplicates
list        Yes         Yes             Yes
set         No          No              No
dict        No          Yes             No
tuple       Yes         No              Yes
'''