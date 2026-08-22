class Person:#Parent class
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name= last_name
    
    def printDetails(self):
        print(f"My first name is {self.first_name} and my last name is {self.last_name}")



# class Student(Person):
#     def __init__(self,first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age     = age

#     def printDetails(self):
#         print(f"My first name is {self.first_name} and my last name is {self.last_name} and my age is {self.age}")
class Student(Person):
    def __init__(self, first_name, last_name, age, hobby):
        # Person.__init__(self,first_name, last_name)
        super().__init__(first_name, last_name)
        self.age = age
        self.hobby = hobby

    def printDetails(self):
        print(f"My first name is {self.first_name} and my last name is {self.last_name} and my age is {self.age}")

    def printHobby(self):
        print(f"My hobby is to do {self.hobby}")
    def printWelcome(self):
        print("Welcome to the school")
person_1 = Person("Aanya","Goyal")
person_1.printDetails()
# person_1.printWelcome() parent can't access the qualities of child

student_1 = Student("Ishaan", "Goyal",13,"Arcylic Painting")
student_1.printDetails()
student_1.printHobby()

