# TODO: String Formatting

# HackerRank STDIN parameters test case 0
# n = int(2)


def print_formatted(num):
    for i in range(1, num+1):
        print("{0:{w}} {0:{w}o} {0:{w}X} {0:{w}b}" .format(i, w=len(bin(num)[2::])))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
