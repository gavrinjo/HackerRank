# TODO: Day 16: Exceptions - String to Integer

"""
TODO: Objective
Today, we're getting started with Exceptions by learning how to parse an integer from a string and
print a custom error message. Check out the Tutorial tab for learning materials and an instructional video!

TODO: Task
Read a string, "S", and print its integer value; if "S" cannot be converted to an integer, print Bad String.

Note: You must use the String-to-Integer and exception handling constructs built into your submission language. If
you attempt to use loops/conditional statements, you will get a 0 score.

"""

import sys

S = input().strip()

try:
    i = int(S)
    print(i)
except ValueError:
    print("Bad String")