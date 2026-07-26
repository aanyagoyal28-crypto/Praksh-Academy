'''
1. Formatting with % operator - covered
2. Formatting with format() string method - covered
3. Formatting with string literals, called f-strings - covered
4. Formatting with String Template class
5. Formatting with center() string method

'''
#"My name is %s I'm eighteen years old" %'Aanya'

print("My name is %s I'm eighteen years old" %'Aanya')#informative purpose - this is old formatting method. 
name="Aanya"
print(f"My name is {name} I'm eighteen years old")

print("My name is %s . I live in %s"%('Oman',name))#order matters the most here. 

pi = 3.1415926535

# %a.bf. a = total number of digits(optional), b = number of digits after decimal point, f = float
print("Value of pi is %.3f"%pi)

weight = 80.4623123

print("My weight is %.2f"%weight)


number = 1936

'''
string - %s
number - %d
float - %f

'''
print("My great grandfather's birth year is %d \n So I got a cake prepared of weight %f grams "%(number,number))#old method v1
# print(f"My great grandfather's birth year is {number} and for supprise I gifted him a car with number plate {float(number)}")


#format() method demonstration v2
print("Format function method - My great grandfather's birth year is {} and for supprise I gifted him a car with number plate {}".format(number,float(number)))

#v3
print(f"My great grandfather's birth year is {number} and for supprise I gifted him a car with number plate {float(number)}")


#indexed based string formatting

print("{4} {2} {1} {0} {3}".format('My','name','is','Aanya','Goyal'))#0,1,2,3,4


#String Template Class - reminder - to reiterate in class and objects module

from string import Template

sentence_1 = "My name is Aanya"
sentence_2 = "Oman"

object_1 = Template('$sentence_3. I live in $sentence_4')#here object_1 is a key to access all the functions in Template class
print(object_1.substitute(sentence_3=sentence_1,sentence_4=sentence_2))

country = 'Oman'
print(country.center(30))

#split()
string_1 = 'My , name,is, Aanya'
string_2='Aanya'

print(string_1.split(','))
print(string_2.split(' '))

#csv - comma separated values


list1 = ["Aanya", "Ishaan", "Rohit", "Seema"]
#Aanya-Ishaan-Rohit-Seema

print(" - ".join(list1))
#join is used to stitch the different characters in a collective datatype
print(" a ".join("My name is Aanya"))#+ is for joinig/attaching two string 

#validations

name = input("Enter your name = ")#isdigit(), startswith, endwith
if (name.lower()).startswith("std"):
    print("Name is ",name)
else:
    print("Enter only characters")