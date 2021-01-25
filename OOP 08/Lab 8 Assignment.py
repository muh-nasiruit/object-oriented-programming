'''
Task 2:

Create an ABC class of Bank and add some abstract method AccountName, 
rate of interest, deposit, withdraw,
Now add some classes in which you will implement 
Bank abstract class and its methods.

'''


from abc import ABC, abstractmethod

class Bank(ABC):
    
    def AccountName(self):
        pass
    
    def IntRate(self):
        pass
    
    def Deposit(self):
        pass
    
    def Withdraw(self):
        pass
    
class AutoMotors(Bank):
    
    def AccountName(self):
        print("Company Account.\n")
        
    def IntRate(self):
        print("2.5% Annual Interest Rate.\n")
    
    def Deposit(self):
        print("Company revenue deposited.\n")
        
    def Withdraw(self):
        print("Money withdrawal successful.\n")
        
class Customer(Bank):
    
    def AccountName(self):
        print("Savers Account.\n")
        
    def IntRate(self):
        print("1.5% Annual Interest Rate.\n")
        
    def Deposit(self):
        print("Savings Deposited.\n")
        
    def Withdraw(self):
        print("Money withdrawal successful.\n")
        
        
        
c1 = AutoMotors()
c2 = Customer()


for i in (c1,c2):
    i.AccountName()
    i.IntRate()
    i.Deposit()
    i.Withdraw()

        
'''
Task 3:
    
Find out one real world example of abstract class 
and abstract method and implement it 
by using python code.

'''


class OnlineSystem(ABC):
    
    def AccountType(self):
        pass
    
    def Courses(self):
        pass
    
    def Transaction(self):
        pass

class Student(OnlineSystem):
    
    def AccountType(self):
        print("Student Account.\n")
        
    def Courses(self):
        print("Student is enrolled in 6 courses.\n")
        
    def Transaction(self):
        print("Student has paid subscription fee.\n")
        

class Teacher(OnlineSystem):
    
    def AccountType(self):
        print("Teacher Account.\n")
        
    def Courses(self):
        print("Teacher is assigned 2 courses.\n")
        
    def Transaction(self):
        print("Teacher has been paid subscription fee.\n")
        
s1 = Student()
t1 = Teacher()
        
def info(x):
    x.AccountType()
    x.Courses()
    x.Transaction()

info(s1)
info(t1)
        
        

































