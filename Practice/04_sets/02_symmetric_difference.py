# Symmetric Difference

"""
TODO: Task
Given "2" sets of integers, "M" and "N", print their symmetric difference in ascending order. The term symmetric
difference indicates those values that exist in either "M" or "N" but do not exist in both.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

# num_a = input()
a = set(list(map(int, input().split())))
# num_b = input()
b = set(list(map(int, input().split())))
myset = set()
myset.update(a.difference(b))
myset.update(b.difference(a))
x = list(map(int, myset))
x.sort()
for i in x:
    print(i)