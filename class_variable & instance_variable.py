class Student:

    # Class variable
    college = "ABC College"

    # Constructor
    def __init__(self, name, branch, marks):
        # Instance variables
        self.name = name
        self.branch = branch
        self.marks = marks

    # Method to display student details
    def display(self):
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Marks:", self.marks)
        print("College:", self.college)
        print("--------------------")


# Creating objects
s1 = Student("Shivani", "CSE", 85)
s2 = Student("Ravi", "ECE", 78)

# Display details
s1.display()
s2.display()