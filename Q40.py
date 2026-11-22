# Question 40: Write a program to print all prime numbers within a given range.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
start_range = 10
end_range = 50

print(f"Prime numbers between {start_range} and {end_range}:")
for val in range(start_range, end_range + 1):
    if val > 1:
        prime = True
        for i in range(2, int(val ** 0.5) + 1):
            if val % i == 0:
                prime = False
                break
        if prime:
            print(val, end=" ")
print()
