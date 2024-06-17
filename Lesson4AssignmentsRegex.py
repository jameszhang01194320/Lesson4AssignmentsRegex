# Lesson 4: Assignments | Regex
# Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!
# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

# 1. Python Regular Expressions Mastery

# Task 1: Name Verification

# Problem Statement:  Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.
# Use the following list as an argument to test your function.
# names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

import re

def verify_names(names):
    # Define the regex pattern for a valid name
    pattern = r'^[A-Z][a-z]*( [A-Z][a-z]*)*$'
    
    for name in names:
        if re.match(pattern, name):
            print(name)
        else:
            print("Invalid name")

# Test the function with the given list of names
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]
verify_names(names)

