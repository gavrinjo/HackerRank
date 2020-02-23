# TODO: Day 11: 2D Arrays
# TODO: Task: Calculate the hourglass sum for every hourglass in [A], then print the maximum hourglass sum.

# Constraints
# -9=<A[i][j]=<9
# 0=<i,j=<5

if __name__ == '__main__':
    """
    HackerRank STDIN parameters test case 0
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    """
    # sample 2D array
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]
    res = []
    for x in range(0, 4):
        for y in range(0, 4):
            s = sum(arr[x][y:y + 3]) + arr[x + 1][y + 1] + sum(arr[x + 2][y:y + 3])
            res.append(s)
    # res = sorted(res)
    # res.reverse()
    # print(res[0])
    print(max(res))
