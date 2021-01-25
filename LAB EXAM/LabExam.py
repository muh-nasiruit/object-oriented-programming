'''
Write a class Time Duration which represents time duration. 
The class should have three fields for hours, minutes and seconds. 
It should have constructor to initialize the hours, minutes and seconds.
A function printDuration() to print the current time. 
Overload the following operators:  - Plus operator (+) to add two Time Duration objects.
(Maintaining minutes and seconds <=60) - Operator < to compare two Time Duration objects.
(Overload these Operator  < operator).

'''

from datetime import datetime, date, time

today = date.today()


class TimeDuration:
    
    def __init__(self, hrs, mins, sec):
        self.hours = hrs
        self.minutes = mins
        self.seconds = sec
        
    def __add__(self, sec):
        hrs = (self.hours + sec.hours)%24
        mins = (self.minutes + sec.minutes)%60
        sec = (self.seconds + sec.seconds)%60
        return TimeDuration(hrs, mins, sec) 
   
    def __str__(self):
        return str(self.hours)+ ':' + str(self.minutes)+ ':' + str(self.seconds)
        
    def __lt__(self, other):
        if (self.hours < other.hours) and (self.minutes < other.minutes) and (self.seconds < other.seconds):
            return True
            # return "Initial Time Duration is less than Final Time Duration."
        
        else:
            return False
            # return "Final Time Duration is less than Initial Time Duration."



    def printDuration(self):
        current = datetime.now()
        print("Current Time =" , current.strftime("%I:%M %p"))
        
        # print("Current Time =" , current.strftime("%H:%M:%S"))
        


# t1 = TimeDuration(12, 32, 13)
# t2 = TimeDuration(22, 80, 5)
# print("Sum of TimeDurations =", t1+ t2)
# print("Comparision: ", t1<t2)

# t = TimeDuration(22,22,22)
# t.printDuration()

# print(" ")


'''
Implement UML diagram. 
Define proper constructor and all member function with appropriate message.
You are free to make necessary assumptions required

'''

class Account:
    
    def __init__(self, Title, name, balance, Type, interest):
        self.title = Title
        self.name = name
        self.balance = balance
        self.type = Type
        self.interest = interest
        
    def Account(self):
        return f"\nTitle: {self.title}\nName: {self.name}\nBalance: Rs.{self.balance}\nAccount Type: {self.type}\nInterest Rate: {self.interest}%\n"

    def getTitle(self):
        return self.title
    
    def setTitle(self, set_title):
        self.title = set_title
    
    def getName(self):
        return self.name
    
    def setName(self, set_name):
        self.name = set_name
    
    def getBalance(self):
        return self.balance
    
    def setBalance(self, set_balance):
        self.balance = set_balance
        
    def getType(self):
        return self.type
    
    def setType(self, set_type):
        self.type = set_type
        
    def getInterest(self):
        return self.interest
    
    def setInterest(self, rate):
        self.interest = rate
        
    def checkBalance(self):
        return f"Remaining Balance: Rs.{self.balance}"
    
    def Deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited: Rs.{amount}") 
    
    def WithDraw(self, value):
        self.balance = self.balance - value
        print(f"WithDrawn: Rs.{value}")
        
    def TransferMoney(self):
        return f"Your Money has been Transfered."


# cust1 = Account("Easy Account", "Muhammad Nasir", 12000, "Savings", 1.7)

# print(cust1.Account())
# cust1.WithDraw(500)
# print(cust1.checkBalance())

# cust1.Deposit(1000)
# print(cust1.checkBalance())

'''
Create an ABC class of Bank and add some abstract method Showinfo,
Location add some classes in then
create sub class Auto, Go, GoMini

'''

from abc import ABC, abstractmethod


class Vehicle(ABC):
    
    @abstractmethod
    def Showinfo(self):
        pass
    
    @abstractmethod
    def Location(self):
        pass
    
class Auto(Vehicle):
    
    def __init__(self, AutoID, rateKM):
        self.AutoID = AutoID
        self.rateKM = rateKM

    def Showinfo(self):
        return f"\nAutoID: {self.AutoID}\nRate/Km: {self.rateKM}"    
   
    def Location(self):
        return f"Vehicle is located in Zone I."

    def setRate(self, rate):
        self.rateKM = rate
        
    def TipCalculation(self):
        tip = self.rateKM *0.2
        print(f"Tip Calculated: Rs.{tip}")


   
class Go(Vehicle):

    def __init__(self, GoldID, rateKM):
        self.GoldID = GoldID
        self.rateKM = rateKM

    def Showinfo(self):
        return f"\nGoID: {self.GoldID}\nRate/Km: {self.rateKM}"

    def Location(self):
        return f"Vehicle is located in Zone II."
 
    def setRate(self, rate):
        self.rateKM = rate 

    def TipCalculation(self):
        tip = self.rateKM *0.3
        print(f"Tip Calculated: Rs.{tip}")




class GoMini(Vehicle):

    def __init__(self, GoMiniID, rateKM):
        self.GoMiniID = GoMiniID
        self.rateKM = rateKM    
    
    def Showinfo(self):
        return f"\nGoMiniID: {self.GoMiniID}\nRate/Km: {self.rateKM}"

    def Location(self):
        return f"Vehicle is located in Zone III."
    
    def setRate(self, rate):
        self.rateKM = rate     
    
    def TipCalculation(self):
        tip = self.rateKM *0.25
        print(f"Tip Calculated: Rs.{tip}")

    
    
# v1 = Go(352, 300)
# print(v1.Showinfo())
# v1.TipCalculation() 
    
    
# v2 = Auto(12, 100)
# print(v2.Showinfo())
# v2.TipCalculation() 
    

class Person:
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
    def Info(self):
        return f"Name: {self.name}\nGender: {self.gender}"
        
class Employee(Person):
    
    def __init__(self,name, gender, empID, position):
        super().__init__(name, gender)
        self.empID = empID
        self.position = position
        
    def Info(self):
        return f"Employee Name: {self.name}\nEmployee ID: {self.empID}"
    


emp1 = Employee("Syed Zain", "Male", 120, "Manager")
person1 = Person("Fatima Tahir", "Female")

for i in (emp1, person1):
    print(i.Info() + '\n')
    







































