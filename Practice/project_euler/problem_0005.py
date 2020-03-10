import math


def compute():
    x = 1
    for i in range(1, 21):
        x *= i // math.gcd(i, x)
    return x
    # moje prvo rješenje!!! ne baš dobro!!!
    # while True:
    #     if all(x % y == 0 for y in range(1, 11)):
    #         break
    #     else:
    #         x += 1


if __name__ == "__main__":
    print(compute())
