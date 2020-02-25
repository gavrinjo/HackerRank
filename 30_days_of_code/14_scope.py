"""
Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and saves it to the "elements" instance variable.
A computeDifference method that finds the maximum absolute difference between any "2" numbers in "N" and stores it in
the "maximumDifference" instance variable.

Constraints
1=<N=<10
1=<elements[i]=<100, where 0=<i=<N-1

"""
class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        pass

    def maximumDifference(self):
        pass


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()
print(a)
print(d.maximumDifference)