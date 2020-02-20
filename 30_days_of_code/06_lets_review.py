# TODO: Day 6: Let's Review

# Enter your code here. Read input from STDIN. Print output to STDOUT

# HackerRank STDIN parameters test case 0
# t = int(2)
# s = Hacker Rank

t = int(input())

for i in range(t):
    s = input()
    print(s[::2], s[1::2])
