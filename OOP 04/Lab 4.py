'''

Task1: Define what you understand by the classes, objects and 
functionalities for the following scenarios.

'''
'''
[in Word]
'''
'''

Task 2: Shape classes and its sub classes and its parameters.


'''

class shape:
    
    length = 0
    width = 0
    height = 0
    radius = 0
    
    def area(self):
        print("Calculating Area... \n")
    
    def perimeter(self):
        print("Calculating Perimeter... \n")

class square(shape):
    
    length = 0
    
    def area(self):
        return self.length * self.length
    
    def perimeter(self):
        return self.length * 4

s1 = square()
s1.length = 10
print("The area of square is: ", s1.area())
print("The perimeter of square is: ", s1.perimeter()) 

class rectangle(shape):
    
    length = 0
    width = 0
    
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return (2 * self.width) + (2 * self.length)

r1 = rectangle()
r1.length = 3
r1.width = 4
print("The area of rectangle is: ", r1.area())
print("The perimeter of rectangle is: ", r1.perimeter())

from math import *

class circle(shape):
    
    radius = 0
    
    def area(self):
        return pi * (self.radius**2)
    
    def perimeter(self):
        return pi * (2 * self.radius)
    
c1 = circle()
c1.radius = 10
print("The area of circle is: {:.5}".format(c1.area()))
print("The perimeter of circle is: {:.5}".format(c1.perimeter()))

print("")


'''

Task 3: Create Book class and sub classes.

'''

class Book: 
    
    title = ""
    author = ""
    
    def __init__(self, subject, pages, back):
        self.subject = subject
        self.pages = pages
        self.back = back
        
    def bookdetails(self):
        return "{} is written by: {}\nPages: {}\n".format(self.title, self.author,
                                                          self.pages)

class English(Book):
    
    def bookinfo(self):
        print("This is an English Book.\n")

class Maths(Book):
    
    def bookinfo(self):
        print("This is a Mathematics Book.\n")

class Science(Book):
    
    def bookinfo(self):
        print("This is a Science Book.\n")

b = Book("English", 32, "Soft")
b.title = "The Adventure"
b.author = "Michael Bay"

print(b.bookdetails())

eng = English("English", 400, "Hard")
eng.bookinfo()

mth = Maths("Maths", 420, "Soft")
mth.bookinfo()





'''

Task 4: Create Courses in CS and SE under the class of CS Program. 
Make methods that can add courses in semester and return it.


'''

class CSProgram:
    
    country = ""
    city = ""
    university = ""
    campus = ""
    applicants = 0
    
    def __init__(self, lecturer, credithours):
        self.lecturer = lecturer
        self.credihours = credithours

class CS(CSProgram):
    
    
    society = ""
    labs = 0
    funds = 0
    semesters = 0
    courses = []
    
    def addcourse(self, course):
        CS.courses.append(course)
        self.semesters =+ self.semesters + 1
    


c1 = CS("Faisal", 3)
c1.addcourse("PF")
c1.addcourse("ICT")
print(c1.courses)
print("Your CS Program now has: ", c1.semesters, "semesters.\n")

print("")


class SE(CSProgram):
    
    
    society = ""
    labs = 0
    funds = 0
    semesters = 0
    courses = []
    
    def addcourse(self, course):
        SE.courses.append(course)
        self.semesters =+ self.semesters + 1
        
s1 = SE("Nasir", 3)
s1.addcourse("Calculus")
s1.addcourse("Islamiat")
s1.addcourse("Communication Skills")
print(s1.courses)
print("Your CS Program now has: ", s1.semesters, "semesters.\n")


    
        




























