

k, arr = int(input()), list(map(int, input().split()))

print(((sum(set(arr))*k)-sum(arr))//(k-1))