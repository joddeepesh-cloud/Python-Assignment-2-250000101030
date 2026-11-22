# Question 28: Write a program to check whether a character is a vowel or consonant.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
char = 'e'
lower_char = char.lower()

if lower_char.isalpha() and len(lower_char) == 1:
    if lower_char in ['a', 'e', 'i', 'o', 'u']:
        print(f"'{char}' is a VOWEL.")
    else:
        print(f"'{char}' is a CONSONANT.")
else:
    print(f"'{char}' is not an alphabetic letter.")
