'''
for loop - This concept is used to do repetitive tasks. 
Syntax : 
for variable in [range(), collective_data_types]:
    code
    code

range(a,b,c) - this function generates a sequence
a - start value(inclusive)(optional)(default =
b - end value(exclusive)(not optional)
c - step value(difference between the series)(optional)(default=1)
rule:
range(1,5)-1,2,3,4
range(6) - 0,1,2,3,4,5(start value will be default  = 0)
range()
if range has one value it is end, if 2 values those are start and end, and if 3 values those are start, end and step
(20,2)
'''

# num = int(input("Enter a number till which you want the natural number series to be generated = "))

# for i in range(0,num,2):
#     print(i)

'''
pass, continue and break
continue - if a condition satisfies the current iteration is skipped
break - if a condition is satisfied the loop is stopped

e.g we have to print a sequence of even digits til the number by the user
whenever you are using contiue, break inside loops using conditional statements is mandatory(logically)

choose for loop when you know the particular number of iterations.

else can be used with for loop this will execute only if the loop exectues completetly without making it terminated by using break keyword
'''

# for i in range(num):
#     break

for i in [1,2,3,4,5]:
    if i==5:
        break
    else:
        print(i)
else:
    print("Loop executed successfully")