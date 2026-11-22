# Question 07: Write a program to calculate the result of an arithmetic expression using multiple operators.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Expression: 10 + 20 * 2 - 15 / 3 + 2 ** 3
# Precedence: ** (exponentiation) -> *, / -> +, -
result = 10 + 20 * 2 - 15 / 3 + 2 ** 3

print("Expression: 10 + 20 * 2 - 15 / 3 + 2 ** 3")
print("Step-by-step breakdown:")
print("  2 ** 3   = 8")
print("  20 * 2   = 40")
print("  15 / 3   = 5.0")
print("  10 + 40 - 5.0 + 8 = 53.0")
print("Result of evaluation:", result)
