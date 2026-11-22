# Question 33: Write a program to calculate the sum of the first N natural numbers.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
n = 50
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"Sum of the first {n} natural numbers is: {total_sum}")
# Verification using n*(n+1)//2
print(f"Formula check: {n * (n + 1) // 2}")
