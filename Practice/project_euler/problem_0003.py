"""
TODO: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

# n = int(13195)
from math import sqrt, floor

# n = int(input("enter number of prime numbers you want to print out?\n"))

"""
def isPrime(n):
    if n == 2:
        return True
    elif n < 1 or not n % 2:
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if not n % i:
            return False
    else:
        return True


def primesList(num):
    primes = [2, ]
    # noPrimes = 1
    testNum = 3

    while testNum < floor(sqrt(num))+1:
        if isPrime(testNum):
            primes.append(testNum)
            # noPrimes += 1
        testNum += 1
    return primes


def fList(n):
    res = []
    plist = sorted(primesList(n))
    x = n
    for i in plist:
        if x % i == 0:
            x = x / i
            res.append(i)
            # print(res)
        else:
            continue

    return res


print(max(fList(int(input()))))
"""


def calculate(n):
    k = n
    while True:
        p = minPrime(k)
        if p < k:
            k //= p
        else:
            return k


def minPrime(n):
    assert n >= 2
    for i in range(3, floor(sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n




if __name__ == '__main__':
    num = int(input())
    print(calculate(num))
