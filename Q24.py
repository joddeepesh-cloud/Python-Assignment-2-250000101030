# Question 24: Write a program to find the greatest among three numbers.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
a = 45
b = 78
c = 62

print(f"Numbers: a = {a}, b = {b}, c = {c}")

if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print(f"The greatest number is: {greatest}")
