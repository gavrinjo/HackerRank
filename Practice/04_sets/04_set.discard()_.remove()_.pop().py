# Set .discard(), .remove() & .pop()

"""
.remove(x)
This operation removes element "x" from the set.
If element "x" does not exist, it raises a KeyError.
The .remove(x) operation returns "None".

.discard(x)
This operation also removes element "x" from the set.
If element "x" does not exist, it does not raise a KeyError.
The .discard(x) operation returns "None".

.pop()
This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a KeyError.

TODO: Task
You have a non-empty set "s", and you have to execute "N" commands given in "N" lines.

The commands will be pop, remove and discard.
"""

n = int(input())
s = set(map(int, input().split()))
l = int(input())

for _ in range(l):
    x = input().split()
    command = x[0]
    argument = x[1:]
    eval("s.{}{}".format(command, tuple(map(int,argument))))

print(sum(s))

