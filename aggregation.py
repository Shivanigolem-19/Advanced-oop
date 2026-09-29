# Teacher class → has name
# School class → receives an already-created Teacher object
# Create a teacher named "Ravi"
# Create a school using that teacher
# Print the teacher's name through the school

class Teacher:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self, Teacher):
        self.Teacher = Teacher

teacher= Teacher("Ravi")

school= School(teacher)

print(school.Teacher.name)