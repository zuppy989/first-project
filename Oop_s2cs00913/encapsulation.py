class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.__age
    
p1 = Person("John", 36)

print(p1.name)
print(p1.get_age()) #Error because  ___age is private