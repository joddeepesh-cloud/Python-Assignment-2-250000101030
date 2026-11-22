# Question 48: Write a program to demonstrate the else clause of a for loop.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
print("Example 1: for loop finishes completely without break")
for i in range(1, 4):
    print("Loop iteration:", i)
else:
    print("For loop completed normally - else block executed!\n")

print("Example 2: for loop terminates with break")
for i in range(1, 4):
    if i == 2:
        print("Breaking loop at i =", i)
        break
else:
    print("This else block will NOT be executed.")
