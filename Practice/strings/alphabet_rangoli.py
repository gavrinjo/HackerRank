# Alphabet Rangoli

"""
size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""


def print_rangoli(size):
    # your code goes here
    s = "abcdefghijklmnopqrstuvwxyz"
    pattern = ["-".join(s[size-1:i:-1] + s[i:size:]).center((size*4)-3, "-") for i in range(0, size)]
    print("\n".join(pattern[::-1] + pattern[1::]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)