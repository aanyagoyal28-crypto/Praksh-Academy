'''
string - 'Aanya' 0-A, 1-a, 2-n, 3-y, 4-a
list - [Aanya]

keynotes:
1. List items are ordered
2. List items are changeable
3. List allows duplicate values
4. If using class method of initializing a list, we need to use double brackets and we should not have the variable name as list, as it is a reserved keyword in python.
'''
list_new=['mango', 'apple', 'guava', 'watermelon', 'papaya','pineapple']#latest way we use to create a list
# list_old = list(('Aanya','Rohit','Goyal'))#old way to create a list
# print(list_old)
# print(type(list_old))
# print(len(list_old))
# print(list_new)
# print(type(list_new))
# print(len(list_new))
string='Aanya'
# for i in list_new:
#     print(i)
print(list_new[-1])#Aanya
print(list_new[2:5])

'''
membership operators
in - if a value is present in the collection 
not in vice versa of in

'''

# desired_fruit=input("Enter a fruit name to check if it is availble = ")
# if desired_fruit.lower() in list_new:
#     print(f"{desired_fruit} is available")
# else:
#     print(f"{desired_fruit} is not available")

# print(list_new)
# list_new[2]='kiwi'#replacing the value
# print(list_new)
# list_new.insert(2,'guava')#insert wil not replace the value, it will add the value at the index and shift the rest of the values to the right
# print(list_new)

# #add a item to the list
# list_new.append('banana')
# print(list_new)

# list_new_1=['red','yellow','green','white','black']
# list_new.extend(list_new_1)#extend will add the values of list_new_1 to
# print(list_new)
# list_new_1.extend(list_new)#extend will add the values of list_new_1 to
# print(list_new_1)

# list_new_1.pop(5)#if you know the index.
# print(list_new_1)

# remove_item=input("Enter the item you want to remove = ")
# if remove_item in list_new_1:
#     list_new_1.remove(remove_item)#if you know the value.
#     print(list_new_1)
# else:
#     print(f"{remove_item} is not present in the list")

#need to print a multiples of any value in a list of entered nujber
list_test = [2,6,3,8,29,56,356,87,13,67]
number = int(input("Enter a number = "))
print("length = ",len(list_test))
print(list_test)
for i in range(len(list_test)):#range(10)#0,1,2,3,4,5,6,7,8,9
    print(list_test[i]*number)

