# Question 26: Write a program to check whether a person is eligible to vote.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
age = 19
MIN_VOTING_AGE = 18

print(f"Person's age: {age}")
if age >= MIN_VOTING_AGE:
    print("Eligible to vote in elections.")
else:
    print(f"Not eligible to vote. Wait for {MIN_VOTING_AGE - age} more year(s).")
