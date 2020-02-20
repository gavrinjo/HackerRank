# TODO: Day 2: Operators

import math
import os
import random
import re
import sys

# HackerRank STDIN parameters test case 0
# meal_cost = float(12.00)
# tip_percent = int(20)
# tax_percent = int(8)

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = float(meal_cost * (tip_percent/100))
    tax = float(meal_cost * (tax_percent/100))
    print(round(meal_cost + tip + tax))

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)
