# Question 35: Write a program to print the multiplication table of a given number.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
number = 7

print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number:>2} x {i:>2} = {number * i:>3}")
