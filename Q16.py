# Question 16: Write a program to demonstrate left-shift and right-shift operators.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
num = 8  # binary: 1000

# Left shift (<< n) multiplies by 2^n
left_shifted = num << 2  # 8 * 4 = 32

# Right shift (>> n) floor divides by 2^n
right_shifted = num >> 2  # 8 // 4 = 2

print(f"Original number        : {num} (bin: {bin(num)})")
print(f"Left-shift by 2 (<< 2) : {left_shifted} (bin: {bin(left_shifted)})")
print(f"Right-shift by 2 (>> 2): {right_shifted} (bin: {bin(right_shifted)})")
