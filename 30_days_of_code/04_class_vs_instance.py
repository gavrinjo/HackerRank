# TODO: Day 4: Class vs. Instance

# HackerRank STDIN parameters test case 0
# t = int(4)
# age = -1 10 16 18

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = 0
        if initialAge < 0:
            print(f"Age is not valid, setting age to {self.age}.")
        else:
            self.age = initialAge


    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age < 13:
            print("You are young.")
        elif age in range(13, 18):
            print("You are a teenager.")
        else:
            print("You are old.")


    def yearPasses(self):
        # Increment the age of the person in here
        global age
        age += 1
        return age


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")