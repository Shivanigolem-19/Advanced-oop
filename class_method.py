class student:
    college = "XYZ college"

    def __init__(self, name, branch):
        self.name = name
        self.branch = branch


    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

s1 = student("Shivani", "CSE")
s2 = student("Ashmitha", "CSD")

print("Name=", s1.name, "\n", "Branch=", s1.branch, "\n", "College=", s1.college)
print("----------------------------------------")
print("Name=", s2.name, "\n", "Branch=", s2.branch, "\n", "College=", s2.college)

student.change_college = "ABC college"

print("----NEW COLLEGE NAME----")
print(student.change_college)