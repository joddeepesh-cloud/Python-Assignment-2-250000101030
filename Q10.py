# Question 10: Write a program to calculate the sum of the digits of a two-digit number.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
number = 87

tens_digit = number // 10
units_digit = number % 10
sum_of_digits = tens_digit + units_digit

print(f"Two-digit number: {number}")
print(f"Tens digit      : {tens_digit}")
print(f"Units digit     : {units_digit}")
print(f"Sum of digits   : {sum_of_digits}")
