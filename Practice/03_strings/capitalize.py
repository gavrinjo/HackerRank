# TODO: Capitalize!

# Complete the solve function below.


def solve(s):
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s


if __name__ == '__main__':
    # commented lines are HR non-editable lines

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
