'''
1. Create a class People and Birthday and perform the composition

Create class People and Birthday which contains instance variables and also implement
following methods printDetails()to print the information

'''

class Birthday:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def birthDate(self):
        return f"{self.day}th of {self.month},{self.year}"

class Person:
    def __init__(self, name, age, birthdate):
        #birthdate FORMAT: "DD/MM/YYYY"
        
        self.x = birthdate
        y = self.x.split('/')
        self.name = name
        self.age = age
        self.day = y[0]
        self.month = y[1]
        self.year = y[2]
        self.hbd = Birthday(self.day, self.month, self.year)
        
    def info(self):
        return f"Name: {self.name}\nAge: {self.age}"

    def printDetails(self):
        return f"{self.name} is {self.age}yrs old.\nHe was born on {self.hbd.birthDate()}."
    
p1 = Person("Ahmed", 17, '20/July/2020')
print(p1.printDetails())






