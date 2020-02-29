# TODO: Practice / Python / Strings / Text Wrap

import textwrap

# HackerRank STDIN parameters test case 0
# string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# max_width = 4


def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
