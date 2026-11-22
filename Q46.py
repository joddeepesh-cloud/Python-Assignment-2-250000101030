# Question 46: Write a program to print numbers from 1 to 20 while skipping multiples of 3 using continue.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
print("Numbers from 1 to 20 skipping multiples of 3:")
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()
