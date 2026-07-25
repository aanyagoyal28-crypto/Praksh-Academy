'''

We cannot modify the strings from their original version the version remains as it is we only make change on their copy created at runtime

string is immutable
'''

country=input('Enter your country name = ')#India
print(country)#India
print(country.upper())
country_uppercase = country.upper()
print("country_uppercase= ",country_uppercase)#INDIA

database_country_value = 'oman'
print(country.lower()==database_country_value)

'''
Client asked to print a string in the exact below format

My name is "Prabhanjan", I mentor "Aanya"

'''

print("My name is \"Prabhanjan\", \nI mentor\t\"Aanya\"")

print('My name is "Prabhanjan", I mentor"Aanya"')

string1="abcdlasjflksjfksjflksjlkfsjlkfjsdlkfjksd"
print(string1.lower())
print("length of string1 is",len(string1))

