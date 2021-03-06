# TODO: Day 17: More Exceptions

"""
Objective
Yesterday's challenge taught you to manage exceptional situations by using try and catch blocks. In
today's challenge, you're going to practice throwing and propagating an exception. Check out the Tutorial tab for
learning materials and an instructional video!

Task
Write a Calculator class with a single method: int power(int,int). The power method takes two integers,
"n" and "p", as parameters and returns the integer result of "n**p2. If either "n" or "p" is negative,
then the method must throw an exception with the message: n and p should be non-negative.

Note: Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.
"""

#Write your code here
class Calculator:

    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError("n and p should be non-negative")

        x = pow(n, p)
        return x


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans=myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
