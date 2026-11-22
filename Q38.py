# Question 38: Write a program to calculate the sum of digits of a given number.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
num = 4589
temp = abs(num)
sum_of_digits = 0

while temp > 0:
    sum_of_digits += (temp % 10)
    temp //= 10

print(f"Sum of digits of {num}: {sum_of_digits}")
