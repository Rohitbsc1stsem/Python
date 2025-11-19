class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name: ", self.name)
        print("Roll No: ", self.roll)

s1 = Student("Rohit",35)
s1.display()