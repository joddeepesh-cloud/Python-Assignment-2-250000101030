# Question 41: Write a program to print the following pattern using nested loops: * / ** / *** / **** / *****.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Desired Pattern:
# *
# **
# ***
# ****
# *****

rows = 5
print("Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
