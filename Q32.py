# Question 32: Write a program to print all even numbers between 1 and 100.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
print("Even numbers between 1 and 100:")
for i in range(2, 101, 2):
    print(i, end=" " if (i // 2) % 10 != 0 else "\n")
