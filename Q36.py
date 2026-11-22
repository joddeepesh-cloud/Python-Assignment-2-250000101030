# Question 36: Write a program to reverse a given integer using a while loop.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
original_num = 12345
num = original_num
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num //= 10

print(f"Original Number : {original_num}")
print(f"Reversed Number : {reversed_num}")
