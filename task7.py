import math

# 1. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2*C*D)/H]
class Formula:
    def __init__(self):
        self.c = 50
        self.h = 30
        self.d = int(input("Enter your value: "))

    def calculate(self):
        result = math.sqrt((2 * self.c * self.d) / self.h)
        print(result)

formula_obj = Formula()
formula_obj.calculate()

# 2. Define a class named Shape and its subclass Square. The Square class has an init
# function which takes length as argument. Both classes have an area function which can
# print the area of the shape where Shape’s area is 0 by default.
class Shape:
    def __init__(self, length):
        self.length = length
        area = 0
        print(area)

class Square(Shape):
    def calculate_area(self):
        area = self.length ** 2
        print(area)

shape_obj = Shape(3)
square_obj = Square(4)
square_obj.calculate_area()

# 3. Create a class to find three elements that sum to zero from a set of n real numbers
class ThreeSum:
    def __init__(self, arr):
        self.arr = arr
        self.res = []

    def three_sum(self):
        self.arr.sort()
        for i in range(len(self.arr)):
            if self.arr[i] > 0:
                break
            if i == 0 or self.arr[i - 1] != self.arr[i]:
                self.two_sum(i)
        print(self.res)

    def two_sum(self, i):
        lo, hi = i + 1, len(self.arr) - 1
        while (lo < hi):
            sum = self.arr[i] + self.arr[lo] + self.arr[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                self.res.append([self.arr[i], self.arr[lo], self.arr[hi]])
                lo += 1
                hi -= 1
                while lo < hi and self.arr[lo] == self.arr[lo - 1]:
                    lo += 1

three_sum_obj = ThreeSum([-25, -10, -7, -3, 2, 4, 8, 10])
three_sum_obj.three_sum()

# 4. Create a Time class and initialize it with hours and minutes.
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add_time(self, hrs, mins):
        self.hrs = hrs
        self.mins = mins
        self.hrs += self.hours
        self.mins += self.minutes
        if self.mins >= 60:
            self.hrs += 1
            self.mins -= 60
        return self.hrs, self.mins

    def display_time(self):
        print(f"{self.hrs} Hours and {self.mins} Minutes")

    def display_minutes(self, hour, minute):
        self.hrs = hour
        self.mins = minute
        total = 0
        if self.hrs > 0:
            total += self.hrs * 60
            total += self.mins
        print(f"{total} Minutes")

time_obj = Time(1, 50)
time_obj.add_time(2, 50)
time_obj.display_time()
time_obj.display_minutes(1, 2)

# 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:
# yearPasses() should increase age by the integer value that you are passing inside the function.
# amIOld() should perform the following conditional actions:I
# f age is between 0 and <13, print “You are young”.
# If age is >=13 and <=19 , print “You are a teenager”.
# Otherwise, print “You are old”.
class Person:
    def __init__(self, age):
        if age > 0:
            self.age = age
        else:
            self.age = 0
            print ("Age is not valid, setting age to 0.")

    def year_passes(self, yrs):
        result = self.age + yrs
        print(result)

    def amIOld(self):
        if self.age >= 0 and self.age < 13:
            print("You Are Young!")
        elif self.age >= 13 and self.age <= 19:
            print("You Are A Teenager!")
        else:
            print("You Are Old!")

person_obj = Person(-1)
person_obj.yearPasses(4)
person_obj.amIOld()