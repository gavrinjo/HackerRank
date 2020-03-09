# Set Mutations

"""
We have seen the applications of union, intersection, difference and symmetric difference operations,
but these operations do not make any changes or mutations to the set.

We can use the following operations to create mutations to a set:

.update() or |
Update the set by adding elements from an iterable/another set.

.intersection_update() or &
Update the set by keeping only the elements found in it and an iterable/another set.

.difference_update() or -
Update the set by removing elements found in an iterable/another set.

.symmetric_difference_update() or ^
Update the set by only keeping the elements found in either set, but not in both.

TODO: TASK
You are given a set "A" and "N" number of other sets. These "N" number of sets have to perform some
specific mutation operations on set "A".
Your task is to execute those operations and print the sum of elements from set "A".

Sample Input
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66

Sample Output
38
"""
a = [set(map(int, input().split())) for _ in range(2)][1]
r = int(input())
for _ in range(r):
    cmd = input().split()[0]
    arg = set(map(int, input().split()))
    eval("a.{}({})" .format(cmd, arg))
print(sum(a))

