# TODO: Day 7: Arrays

import math
import os
import random
import re
import sys

# HackerRank STDIN parameters test case 0
# n = int(4)
# arr = 1 4 3 2

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(" ".join(map(str, arr[::-1])))

