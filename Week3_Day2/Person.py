class Person:
    is_alive = True

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


person1 = Person("Luvuyo", 20, "male", "173cm")
print(person1.age, person1.get_name())
