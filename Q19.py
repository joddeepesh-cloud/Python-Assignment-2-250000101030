# Question 19: Write a program to demonstrate identity operators is and is not.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"id(list1) = {id(list1)}")
print(f"id(list2) = {id(list2)}")
print(f"id(list3) = {id(list3)}")

print("list1 == list2     :", list1 == list2, "(Values are equal)")
print("list1 is list2     :", list1 is list2, "(Distinct objects in memory)")
print("list1 is list3     :", list1 is list3, "(Same object reference)")
print("list1 is not list2 :", list1 is not list2)
