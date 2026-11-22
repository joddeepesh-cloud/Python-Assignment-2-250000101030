# Question 44: Write a program to print all pairs of numbers from 1 to 5 using nested loops.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
print("All pairs (i, j) where 1 <= i, j <= 5:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"({i}, {j})", end=" ")
    print()
