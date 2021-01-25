'''

Task 2: Create class and sub classes for different 
types of frequent airline travelers with different
connecting flights. Use concept of Multiple inheritance 
and Super().

'''

class Emirates:
    def __init__(self, status1, flightno1):
        self.status1 = status1
        self.flightno1 = flightno1
    
    def flight_details1(self, fclass1, seat_num1):
        
        print(f"Appointed Seat: {seat_num1}\nIn {fclass1}.\nEnjoy your Emirates Flight!\n")
        
        
class Qatar:
    
    def __init__(self, status2, flightno2):
        self.status2 = status2
        self.flightno2 = flightno2
    
    def flight_details2(self, fclass2, seat_num2):
        
        print(f"Appointed Seat: {seat_num2}\nIn {fclass2}.\nEnjoy your Qatar Flight!\n")
    


class traveler(Emirates, Qatar):
    
    def __init__(self, status1, flightno1, status2, flightno2):
        Emirates.__init__(self, status1, flightno1)
        Qatar.__init__(self, status2, flightno2)
        
    def flight_status(self):
        print("Your initial flight: {}\tStatus: {}\nYour connecting flight: {}\tStatus: {}\n".format(self.flightno1, self.status1, self.flightno2, self.status2))



t1 = traveler("Arrived", 125, "Delayed", 420)
t1.flight_status()
t1.flight_details2("Economy Class", 52)

t2 = traveler("Arrived", 956, "Arrived", 102)
t2.flight_status()
t2.flight_details1("First Class", 12)



'''

Task 3: Create class and sub classes for differenet
types of umbrella, they have different styles, prints,
sizes, for male, female, kids, they have different usage 
such as only for rain, for sun protection for
snow. Etc. Use the concept of Multiple inheritance 
and supper() where necessary.
Classes, use case first then process.

'''


class type_:
    
    def __init__(self, season, gender):
        
        self.season = season
        self.gender = gender
    
    def showinfo(self):
        return f"This umbrella is designed specifically for {self.season} weather.\nFor {self.gender}.\n"
    


class design:
    
    def __init__(self, color, material, prnt, size):
        self.color = color
        self.material = material
        self.prnt = prnt
        self.size = size
        
    def showstyle(self):
        return f"Material: {self.material}\tPrint: {self.prnt}\tSize: {self.size}.\n"

class umbrella(type_ , design):
    
    def __init__(self, season, gender, color, material, prnt, size):
        type_.__init__(self, season, gender)
        design.__init__(self, color, material, prnt, size)
        
    def purchase(self, serial, price, item):
        print("Item Number: {}\nColor: {}\tSize: {}\nTotal: ${} for {} Umbrella.\n".format(serial, self.color, self.size, price, item))
        

u1 = umbrella("Rainy Season", "Male", "Purple", "Polyster", "Polka", 7)

print(u1.showinfo())
print(u1.showstyle())
u1.purchase(7564, 500, 2)
        
u2 = umbrella("Sunny Season", "Female", "Black", "Parachute", "Stripes", 4)

print(u2.showinfo())
print(u2.showstyle())
    
u2.purchase(1002, 800, 1)






















