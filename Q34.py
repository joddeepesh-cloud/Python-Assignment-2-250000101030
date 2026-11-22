# Question 34: Write a program to calculate the factorial of a given number using a loop.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
num = 6
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} ({num}!) is: {factorial}")
