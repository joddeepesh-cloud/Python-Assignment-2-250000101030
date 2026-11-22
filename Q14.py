# Question 14: Write a program to check whether a number is divisible by both 3 and 5 using logical operators.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
num = 45

if (num % 3 == 0) and (num % 5 == 0):
    print(f"{num} is divisible by both 3 and 5 (i.e., divisible by 15).")
else:
    print(f"{num} is not divisible by both 3 and 5.")
