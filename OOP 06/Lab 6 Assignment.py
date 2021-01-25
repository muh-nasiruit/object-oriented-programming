
'''
Case Study 1:

Create a class Employee and derive a child class 
programmer using public inheritance.

    • Create class case diagram.
    • Code the parent and derive classes on python

'''
'''
class Employee:
    
    def __init__(self, company, year):
        self.company = company
        self.year = year
        
    def details(self):
        return "Employeed in: {}. since {}\n".format(self.company, self.year)



class Programmer(Employee):
    
    def __init__(self, name, post, project):
        super().__init__("The Real", 2020)
        
        self.name = name
        self.post = post
        self.project = project
        
    def info(self):
        return "Programmer: {}\nProject: {}\n".format(self.name, self.project)


e1 = Programmer("Akmal", "Junior", "Database")
print(e1.details())
print(e1.info())

e2 = Employee("The Fakes", 1998)
print(e2.details())

e3 = Programmer("Shahid", "Senior", "API")
print(e3.info())

'''


'''    
Case Study 2:

Create a parent class Employee, derive child class 
Programmer and Designer using inheritance

    • Create class case diagram.
    • Code the parent and derive classes on python
    
'''

class Employee:
    
    def __init__(self, company, year):
        self.company = company
        self.year = year
        
    def details(self):
        return "Employeed in: {}. since {}\n".format(self.company, self.year)


class Programmer:
    
    def __init__(self, name, post, project):
        
        self.name = name
        self.post = post
        self.project = project
        
    def info(self):
        return "Programmer: {}\nProject: {}\n".format(self.name, self.project)
    
class Designer(Employee, Programmer):
    
    def __init__(self, company, year, name, post, project, team):
        Employee.__init__(self, company, year)
        Programmer.__init__(self, name, post, project)
        
        self.team = team
        
    def designInfo(self):
        return "Designer: {}, Assigned in: {}\n".format(self.name, self.team)
    

e1 = Designer("The OG", 2020, "Akmal", "Junior", "SEAL", "Marketing Team")
print(e1.details())
print(e1.info())
print(e1.designInfo())





'''


Case Study 3:
    
Analyze the detail system of car loan management system. 
You can take help of internet to find
you any car loan management system. Your task is as follows:

    b. Define all the existing processes in loan management system.
    c. Create classes.
    d. Create use case diagram.
    e. Make activity and sequence diagram.
    f. Now select any class and try to enhance it according to your gap analysis.
    g. Code the class for which you have enhance the process.

'''


class Teller:
    
    def __init__(self, date, bank):
        self.date = date
        self.bank = bank
        
    def intro(self):
        return f"Welcome to {self.bank}!\n\t~{self.date}\n" 

class Loanee:
    
    def __init__(self, Id, balance):
        
        self.Id = Id
        self.balance = balance

    
    def details(self, name, age, gender):
        return f"Name: {name}\nAge: {age}\nGender: {gender}\n"
    
class LMSystem(Teller, Loanee):
    
    def __init__(self, date, bank, Id, balance, currency):
        Teller.__init__(self, date, bank)
        Loanee.__init__(self, Id, balance)
        
        self.currency = currency
        
    def ReqLoan(self, loan):
        return f"Loanee ID: {self.Id}\nhas requested for a loan of,\nLoan Amount:\t${loan}\n"
        
    def LoanStatus(self, status):
        return f"Loan Request Status: {status}\n"
    
    def FeesCollection(self, fees):
        amount = self.balance - fees
        self.balance = amount
        return f"You have been charged:\t${fees}\nRemaining Blanace:\t${amount}\n"
     
'''
l1 = LMSystem("21/11/1999", "Maze Bank", 125, 5000, "Dollars")
print(l1.intro())
print(l1.details("Muhammad Nasir", 21, "M"))
print(l1.ReqLoan(10000))
print(l1.FeesCollection(500))
print(l1.LoanStatus("Approved"))

'''



'''
2. Analyze the detail system of Cargo Management System. 
You can take help of internet to find
you any cargo management system. Your task is as follows:
    
    a. Define all the existing processes in cargo management system.
    b. Create the main classes.
    c. Create use case diagram.
    d. Make activity and sequence diagram.
    e. Now select any class and try to enhance it according to your gap analysis.
    f. Code the class for which you have enhance the process.

'''

class Customer:
    
    def __init__(self, custId, wallet):
        self.custId = custId
        self.wallet = wallet
        
    def info(self, name, address, num):
        return f"Name:\t{self.name}\nPhone Number:\t{self.num}\nAddress:\t{self.address}\n"
    
    def balance(self):
        return f"Remaining Balance:\t${self.wallet}\n"

class Cargo:
    
    def __init__(self, cargId):
        self.cargId = cargId
    
    def details(self, wght, size, cargType):
        return f"Cargo Type:\t{cargType}\nWeight:\t{wght}\nSize:\t{size}\n"
    
    def pack(self):
        print("Your cargo has been packed successfully!")
    
class CMSystem(Customer, Cargo):
    
    def __init__(self, custId, cargId, wallet, delType):
        Customer.__init__(self, custId, wallet)
        Cargo.__init__(self, cargId)
        
        self.delType = delType   
        
    def Receipt(self, item, quantity, price):
        cost = price * quantity 
        self.wallet = self.wallet - cost
        return f"You have purchased:\t{item}\nPrice:\t${price}\nQuantity: {quantity}\nAmount:\t${cost}\n"

    def CargoStatus(self, status):
        return f"Cargo Status:\t{status}\n"

   
c1 = CMSystem(12, 14002, 10000, "Express")
print(c1.Receipt("Steam Wallet", 5, 350))
print(c1.Receipt("Jordans",  2, 500))
print(c1.Receipt("PS5", 1, 1000))
print(c1.balance())























































