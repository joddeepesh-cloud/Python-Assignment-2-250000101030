# Question 08: Write a program to swap two numbers using arithmetic operators.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Swapping using addition and subtraction
a = 25
b = 45

print(f"Before swap: a = {a}, b = {b}")

a = a + b  # a now becomes 70
b = a - b  # b becomes (70 - 45) = 25
a = a - b  # a becomes (70 - 25) = 45

print(f"After swap : a = {a}, b = {b}")
