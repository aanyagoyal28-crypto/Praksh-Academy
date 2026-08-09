'''
dict - a key value pair data structure
syntax : 
variable_name = {
key1:value1,
key2:value2,
key3:value3
}
'''

student_data={
    "name":"Aanya",
    "age":17,
    "grade":"12th"
}

print(len(student_data))
print(student_data["name"])
print(student_data.keys())
print(student_data.values())
print(student_data.items())

print("name" in student_data)

# student_data["name"] = "Aanya Goyal"
student_data.update({"name":"Aanya Sharma"})
print(student_data)

student_data['country']='Oman'
print(student_data)

student_data.pop("country")
print(student_data)

student_data.popitem()
print(student_data)


# del student_data["age"]
# print(student_data)


# student_data.clear()
# print(student_data)

student_data_copy = student_data.copy()
print(student_data_copy)