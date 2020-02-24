# Day 12: Inheritance

"""
TODO: Day 12: Inheritance
Task: You are given two classes, Person and Student, where Person is the base class and Student is the
derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe
that Student inherits all the properties of Person. Complete the Student class by writing the following:
    A Student class constructor, which has 4 parameters:
        A string, "firstName"
        A string, "lastName"
        An integer, "id"
        An integer array (or vector) of test scores, "scores"

A char calculate() method that calculates a Student object's average and returns the grade character representative
of their calculated average:

O 90=<a=<100
E 80=<a<90
A 70=<a<80
P 55=<a<70
D 40=<a<55
T a<40

"""


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):


    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avr = int(sum(self.scores)/len(self.scores))
        if avr in range (90, 101):
            return "O"
        elif avr in range(80, 90):
            return "E"
        elif avr in range(70, 80):
            return "A"
        elif avr in range(55, 70):
            return "P"
        elif avr in range(40, 55):
            return "D"
        else:
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
# numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
