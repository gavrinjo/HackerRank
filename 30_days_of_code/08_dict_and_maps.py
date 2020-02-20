# TODO: Day 8: Dictionaries and Maps

# HackerRank STDIN parameters test case 0
# n = int(3)
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
d = {}

for i in range(n):
    s, b = input().split()
    d[s] = b

while True:
    try:
        line = input()
        if line in d:
            print("{}={}" .format(line, d[line]))
        else:
            print("Not found")
    except EOFError:
        break
