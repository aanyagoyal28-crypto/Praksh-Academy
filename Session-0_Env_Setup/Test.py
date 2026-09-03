print("aanya")
print("testing changes")

class Student:
    x = 5
    def greet(self):
        print("Hello this is student class")


# I have to create an object.
object1 = Student()#constructor of the class
print(object1.x)
object1.greet()

class Greet():
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Good Morning, {self.name}")
        
object1 = Greet("Aanya")
object1.greet()