# Question 20: Write a program to evaluate expressions and demonstrate Python operator precedence.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Operator Precedence (high to low):
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary +, -
# 4. Multiplication *, Division /, Floor //, Modulus %
# 5. Addition +, Subtraction -
# 6. Comparison ==, !=, <, <=, >, >=
# 7. Logical not, and, or

exp1 = 10 + 5 * 2 ** 2
exp2 = (10 + 5) * 2 ** 2

print(f"10 + 5 * 2 ** 2  = {exp1} (2**2=4, 5*4=20, 10+20=30)")
print(f"(10 + 5) * 2 ** 2= {exp2} ((10+5)=15, 2**2=4, 15*4=60)")
