class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Marks :", self.marks)

    @staticmethod
    def is_pass(marks):
        return marks >= 35

    @staticmethod
    def percentage(marks):
        return marks/500

s1= Student("Shivani", 450)
s1.display()

if Student.is_pass(s1.marks):
    print("Result = pass")
else:
    print("Result = fail")

print("Percentage :", Student.is_pass(s1.marks))