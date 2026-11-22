# Question 17: Write a program to check whether a number is even or odd using a bitwise operator.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# If (num & 1) is 0, the number is even; if 1, odd.
num = 27

if (num & 1) == 0:
    print(f"{num} is an EVEN number.")
else:
    print(f"{num} is an ODD number.")
