"""
slicing - it is a operation performed on strings to extract or store the extracted value in other variables

1. Indexing in string starts from 0
e.g Aanya (A-0, a-1, n-2, y-3, a-4)

slicing opeartor:
Syntax [a:b]
a - start value(it is included)
b - end value(it is excluded)
c - step value(the gap in between the characters), by default step=0 discuss this in list variant

reverse:
    0   1  2  3  4
    A   a  n  y  a
    -5 -4 -3 -2 -1

start < step
"""
name = 'Aanya Rohit Goyal'

print(name[2:5])#nya
print(name[6:11])
print(name[12:17])
print(name[-5:])

# string_1 = 'Aeroplane'
# print([::-1])