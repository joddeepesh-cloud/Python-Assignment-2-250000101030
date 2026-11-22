# Question 03: Write a program to calculate the remainder without using the modulus operator.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Remainder formula: remainder = dividend - (divisor * (dividend // divisor))
dividend = 27
divisor = 5

quotient = dividend // divisor
remainder = dividend - (divisor * quotient)

print(f"Dividend: {dividend}, Divisor: {divisor}")
print(f"Quotient: {quotient}")
print(f"Calculated Remainder: {remainder}")
print(f"Verification using % : {dividend % divisor}")
