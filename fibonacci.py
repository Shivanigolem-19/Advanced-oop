# Write a Python program that takes n from the user and prints the first n Fibonacci numbers.
a=0
b=1

for i in range(5):
    print(a)
    temp=a
    a=b
    b=temp+a