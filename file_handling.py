#r-read
file = open("student.txt", "r")

data = file.read()
print(data)

file.close()

# #w-write
# file = open("student.txt", "w")

# file.write("I am learning Python.")

# file.close()

# #a-append
# file = open("student.txt", "a")

# file.write("\nI am learning OOP.")

# file.close()
