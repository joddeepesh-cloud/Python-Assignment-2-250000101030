# Question 43: Write a program to print a multiplication table from 1 to 10 using nested loops.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
print("Multiplication Table from 1 to 10:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4d}", end="")
    print()
