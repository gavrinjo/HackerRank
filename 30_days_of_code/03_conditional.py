# TODO: Day 3: Intro to Conditional Statements

import math
import os
import random
import re
import sys

# HackerRank STDIN parameters test case 0
# n = int(3)

if __name__ == '__main__':
    n = int(input())

if n % 2 == 0 and (n in range(2, 6) or n > 20):
    print("Not Weird")
else:
    print("Weird")