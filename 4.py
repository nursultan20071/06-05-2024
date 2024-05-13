class Person:
    def __init__(self, name, age, surname):
        self.name = name
        self.age = age
        self.surname = surname

    def my_method(self):
        print("Менің атым " + self.name + " " + self.surname)

p1 = Person("Нурс", 16, "Жадырасынов")
p1.my_method()
