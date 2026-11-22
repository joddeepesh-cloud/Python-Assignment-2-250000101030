# Question 47: Write a program to demonstrate the use of the pass statement inside a loop.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
print("Demonstrating 'pass' statement as a placeholder:")
for i in range(1, 6):
    if i == 3:
        # pass does nothing, acts as a syntactic placeholder
        pass
        print(f"At i = {i}, pass was executed without interrupting flow.")
    else:
        print(f"Number: {i}")
