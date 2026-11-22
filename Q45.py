# Question 45: Write a program to demonstrate the use of the break statement in a loop.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
print("Demonstrating 'break' statement:")
print("Searching for number 7 in range 1 to 15:")

for num in range(1, 16):
    if num == 7:
        print(f"Target {num} found! Breaking out of loop.")
        break
    print(f"Checking number: {num}")
