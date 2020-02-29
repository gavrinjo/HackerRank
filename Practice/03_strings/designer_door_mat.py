# TODO: Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
# HackerRank STDIN parameters test case 0


n, m = map(int, input().split())
s = ".|."

for i in range(n//2):
    print((s*i).rjust(m//2-1, "-")+s+(s*i).ljust(m//2-1, "-"))

print("WELCOME".center(m, "-"))

for i in range(n//2):
    print((s*(n//2-i-1)).rjust(m//2-1, "-")+s+(s*(n//2-i-1)).ljust(m//2-1, "-"))
"""
n, m = map(int, input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
"""
