# Question 31: Write a program to print numbers from 1 to 100 using a for loop.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" " if i % 10 != 0 else "\n")
