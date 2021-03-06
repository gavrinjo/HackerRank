"""
Introduction to Sets
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

TODO: Task
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the
average of all the plants with distinct heights in her greenhouse.

Formula used: Average=Sum of Distinct Heights/Total Number of Distinct Heights

"""

def average(array):
    # your code goes here
    num = set(array)
    return sum(num)/len(num)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)