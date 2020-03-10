from math import floor


def calculate(n):
    for i in range(n, floor(n / 1.1), -1):
        for j in range(i, floor(n / 1.1), -1):
            if isPalindrome(i * j):
                return "{} x {} = {}".format(i, j, i * j)
            else:
                continue


def isPalindrome(n):
    div = 1
    while n / div >= 10:
        div *= 10

    while n != 0:
        leading = floor(n / div)
        trailing = n % 10

        # If first and last digit not same return false
        if leading != trailing:
            return False

        # Removing the leading and trailing digit from number
        n = floor((n % div) / 10)

        # Reducing divisor by a factor of 2 as 2 digits are dropped
        div = div / 100
    return True


if __name__ == '__main__':
    nDigits = int(input())
    num = int("9" * nDigits)
    print(calculate(num))
