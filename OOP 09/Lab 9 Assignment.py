
'''
Task 1:
Create a class distance that take feet, 
inches and then perform an operator overloading
(Overload + Operator).

'''

class Distance:
    
    def __init__(self, Ft, In):
        self.feet = Ft 
        self.inch = In
        
    def __add__(self, sec):
        Ft = self.feet + sec.feet
        In = self.inch + sec.inch
        return Distance(Ft ,In)
    
    def __str__(self):
        return str(self.feet)+ '\"' + str(self.inch)+ '\''
    
d1 = Distance(6, 1)
d2 = Distance(5, 3)
d3 = Distance(9, 4)

print("The sum of distances: ", d1+d2)
print("The sum of distances: ", d1+d3)
print("The sum of distances: ", d2+d3)


'''
Task 2:
Create a class time that take hour’s minutes, 
and second and then perform an operator
overloading (Overload - Operator).

'''


class Time:
    
    def __init__(self, h, m, s):
        self.hour = h
        self.min = m
        self.sec = s
    
    def __sub__(self, ex):
        h = self.hour - ex.hour
        m = self.min - ex.min
        s = self.sec - ex.sec
        return Time(h, m, s)
        
    def __str__(self):
        return str(self.hour)+ 'hours '+str(self.min)+'minutes '+str(self.sec)+'seconds'


t1 = Time(3, 20, 9)
t2 = Time(8, 55, 14)
t3 = Time(10, 60, 23)

print("The time difference: ", t2-t1)
print("The time difference: ", t3-t1)
print("The time difference: ", t3-t2)






















