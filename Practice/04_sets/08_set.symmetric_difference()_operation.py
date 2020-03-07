# Set .symmetric_difference() Operation

"""
.symmetric_difference()
The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not
both. Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set
of elements in set. The set is immutable to the .symmetric_difference() operation (or ^ operation).

Task
Students of District College have subscriptions to English and French newspapers. Some students have subscribed to
English only, some have subscribed to French only, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has
subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either
the English or the French newspaper but not both.

Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output
8
"""

a, b = [set(input().split()) for _ in range(4)][1::2]
# x = a.symmetric_difference(b)
print(len(a ^ b))
