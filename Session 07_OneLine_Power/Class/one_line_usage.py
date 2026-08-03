# list_of_marks = [98,70,88,76,93]
# # list_of_corrected_marks=[]
# # for marks in list_of_marks:
# #     list_of_corrected_marks.append(marks - 2)
# list_of_corrected_marks=[marks - 2 for marks in list_of_marks]
# print(list_of_marks)
# # print(list_of_corrected_marks)

list_of_num = [1,2,3,4,5,6,7,8,9,10]
results = [num for num in list_of_num if num%2 == 0]
print(list_of_num)
print(results)


for num in list_of_num:
    if num%2==0:
        results.append(num)