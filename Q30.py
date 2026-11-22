# Question 30: Write a program to calculate electricity charges using different slabs with nested if statements.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Slabs:
# First 100 units       : Rs 2.50 per unit
# Next 100 units (101-200): Rs 3.50 per unit
# Above 200 units       : Rs 5.00 per unit

units = 250
bill = 0.0

print(f"Total Electricity Units Consumed: {units}")

if units <= 100:
    bill = units * 2.50
else:
    # Units exceed 100
    bill = 100 * 2.50
    remaining_units = units - 100
    if remaining_units <= 100:
        bill += remaining_units * 3.50
    else:
        # Remaining units exceed 100
        bill += 100 * 3.50
        bill += (remaining_units - 100) * 5.00

print(f"Total Electricity Bill: Rs. {bill:.2f}")
