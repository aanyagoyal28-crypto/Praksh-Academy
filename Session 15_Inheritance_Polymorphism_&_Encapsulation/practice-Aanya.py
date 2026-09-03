# class Person:
#     def __init__(self, first_name , last_name):
#         self.first_name=first_name
#         self.last_name =last_name

#     def print_details(self):
#         print(f"My first name is {self.first_name} and my last name is {self.last_name}")

# person_1=Person("Aanya", "Goyal")
# print(person_1)
# person_1.print_details()


# class Student(Person):
#     def __init__(self, first_name , last_name, age):
#         super().__init__(first_name, last_name)
#         self.age=age
#     def print_details(self):
#         print(f"My first name is {self.first_name} and my last name is {self.last_name}. My age is {self.age}")
# student_1= Student("Ishaan", "Goyal" , 13)
# print(student_1.first_name)
# student_1.print_details()


# class Animal:
#     def __init__(self, name):
#         self.name=name
#     def animal_sound(self):
#         print("sample")

# class Dog(Animal):
#     def animal_sound(self):
#         print("Bow Bow")
# class Cat(Animal):
#     def animal_sound(self):
#         print("Meow Meow")

# dog=Dog("Dog")
# dog.animal_sound()
# cat=Cat("Cat")
# cat.animal_sound()



class Person:
    def __init__(self, name, age, mob_no):
        self.name=name
        self.age= age
        self.__mob_no=mob_no
    def print_details(self):
        print(f"My name is {self.name} and my age is {self.age} and number is {self.__mob_no}")
    def get_mob_no(self):
        print(self.__mob_no)
    def update_mob_no(self,mob_no):
        self.__mob_no=mob_no

person_1= Person("Aanya", 17, 96290201)
print(person_1)
person_1.print_details()
print(person_1.age)
(person_1.get_mob_no())
person_1.update_mob_no(12456908)
person_1.get_mob_no()



    
        