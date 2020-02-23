# TODO: Day 10: Binary Numbers

# TODO: Task - Given a base -10 integer ,n, convert it to binary (base -2). Then find and print the base -10 integer
#  denoting the maximum number of consecutive 1's in n's binary representation.
"""
import math
import os
import random
import re
import sys
"""
# HackerRank STDIN parameters test case 0
# n = int(5)

if __name__ == '__main__':
    n = int(input())
    lis = "".join(bin(n)[2::]).split("0")
    # lis = sorted(lis)
    # lis.reverse()
    # print(eval("+".join(lis[0])))
    print(max(lis))

