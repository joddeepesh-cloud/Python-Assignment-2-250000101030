# Question 42: Write a program to print the following number pattern using nested loops: 1 / 12 / 123 / 1234 / 12345.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Desired Pattern:
# 1
# 12
# 123
# 1234
# 12345

rows = 5
print("Number Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
