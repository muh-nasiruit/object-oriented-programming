
'''
Task 1: Create a class Point having X and Y axis 
then perform an operator overloading
(Overload all relation operator).


'''

class Point:
    
    def __init__(self, p):
        self.p = p
        
    def __lt__(self, other):
        if (self.p < other.p):
            return "X is less than Y."
            
        else:
            return "X is not less than Y."
    
    def __gt__(self, other):
        if (self.p > other.p):
            return "X is greater than Y."
            
        else:
            return "X is not greater than Y."
            
    def __eq__(self, other):
        if (self.p == other.p):
            return "X is equal to Y."
        
        else:
            return "X and Y are different values."
        
    
    def __ne__(self, other):
        if (self.p != other.p):
            return "X is not equal to Y."
        
        else:
            return "X and Y have similar values."
        
        
# x1 = Point(5)
# y1 = Point(9)

# x2 = Point(3)
# y2 = Point(3)

# print(x1 < y1)
# print(x1 > y1)
# print(x2 == y2)
# print(x1 != y1)
# print(" ")
'''
Task 2:
Find out one real world example of interface and 
implement all abstract method by using python n
code.

'''



from abc import ABC, abstractmethod


class Student(ABC):
    
    @abstractmethod
    def Name(self):
        pass
    @abstractmethod
    def Gender(self):
        pass
    @abstractmethod
    def RollNum(self):
        pass
    
    def Percentage(self, percent):
        return f"\nPercentage acquired: {percent}%"
    
class CR(Student):
    
    def Name(self):
        return "Rashid Ali Abbasi."
        
    def Gender(self):
        return "Male."
        
    def RollNum(self):
        return "1059\n"
        
class TA(Student):
    
    def Name(self):
        return "Khalid Ahmed."
        
    def Gender(self):
        return "Male."
        
    def RollNum(self):
        return "4032"
        


s1 = CR()
m1 = s1.Percentage(95)
print(s1.Name(), m1)
print("")

s2 = TA()
m2 = s2.Percentage(70)
print(f"{s2.Name()} Roll Number: {s2.RollNum()} {m2}")

































