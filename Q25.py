# Question 25: Write a program to check whether a given year is a leap year.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Leap year rule: divisible by 4, but not by 100 unless divisible by 400
year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a LEAP year.")
else:
    print(f"{year} is NOT a leap year.")
