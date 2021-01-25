


'''Task 2: 
    Create class and sub classes for different types of residential houses. Each house object
has different parameters such as number of location of the house, rooms, parking available or not.
Price of the house.


'''
class house:
    
    def __init__(self, location, rooms, parking, price):
        self.location = location
        self.rooms = rooms
        self.parking = parking
        self.price = price 
        
    def details(self, name):
        return "{} is a house located: {}\nhaving rooms: {}\nwith parking: {}\nfor only: {}PKR ".format(name, 
                                                                                            self.location, self.rooms, 
                                                                                            self.parking, self.price) 
    
class bungalow(house):
    
    def b_details(self, name1):
        return "{} is a Bungalow located: {}\n having rooms: {}\n with parking: {}\n for only: {}PKR ".format(name1, 
                                                                                            self.location, self.rooms, 
                                                                                            self.parking, self.price)
    
class cottage(house):
    
    def c_details(self, name2):
        return "{} is a Cottage located: {}\n having rooms: {}\n with parking: {}\n for only: {}PKR ".format(name2,
                                                                                            self.location, self.rooms,
  

                                                                                          self.parking, self.price) 
    
    
house1 = house("ABC Society", 5, "Available", 30000000)
print(house1.details("Grand Villa"))
    
x = bungalow("DHA Phase IV", 7, "Available", 80000000)
print(x.b_details("Maymar Mansion"))

y = cottage("Gulshan e Iqbal", 5, "Not Available", 40000000)
print(y.c_details("Iqbal House"))


'''
Task 3: 
    Create class and sub classes for differ types of vehicles for Toyota Motors. Each car object
belongs to some particular model, color, price, type of car such as saloon, luxury or sports. They
can be registered in different years and made in different years.

'''
class toyota_motors():
    name = "Corolla "
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        
    def displayname(self):
        print('Name: ', self.name)
        
        
class luxury(toyota_motors):
    def classification1(self, classify1):
        
        return "{} is a {}\n having model number:{}\n colored: {}\n for only: {}PKR".format(self.name, classify1, self.model,
                                                                                  self.color, self.price)

class saloon(toyota_motors):
    def classification2(self, classify2):
        
        return "{} is a {}\n having model number:{}\n colored: {}\n for only: {}PKR".format(self.name, classify2, self.model,
                                                                                  self.color, self.price)




a = luxury("AFR20", "Coral", 2000000)
print(a.classification1("Jeep"))

b = saloon("AFR18", "Pink", 1500000)
print(b.classification2("Land Cruiser"))

'''
Task 4: You are hired in a mobile company which produces multiple mobiles each year. Select
any mobile company create one main class, some sub classes, add some features and methods to
operate the mobile and then create some objects for your friends and check how it will work.

'''
class mobile:
    
    manufactured = "Pakistan"
    condition = "New"
    
    def __init__(self, model, OS, memory, camera):
        
        self.OS = OS 
        self.memory = memory
        self.camera = camera
        self.model = model
        
    def displaymsg(self, msg):
        return "Hope you are having a nice day :D\n{}\n".format(msg)
    
    def details(self):
        print("This phone operates on {}\nMemory: {}\nCamera: {}\n".format(self.OS, self.memory, self.camera))
        

class Samsung(mobile):
    
    company = "Samsung"
    
    def info_samsung(self):
        print("Samsung {}, {}, {} GB, {} mpx\n".format(self.model, self.OS, self.memory, self.camera))
        
    def features(self, waterproof, dualsim, ex_mem, sensor):
        print("Additional Features include:\nWaterproof: {}\nDual Sim: {}\nExternal Memory: {}\nFingerprint Sensor: {}\n".format(waterproof, dualsim, ex_mem, sensor))
    

class IPhone(mobile):
    
    company = "IPhone"
    
    def info_iphone(self):
        print("IPhone {}, {}, {} GB, {} mpx\n".format(self.model, self.OS, self.memory, self.camera))
        
    def features(self, waterproof, dualsim, ex_mem, sensor):
        print("Additional Features include:\nWaterproof: {}\nDual Sim: {}\nExternal Memory: {}\nFingerprint Sensor: {}\n".format(waterproof, dualsim, ex_mem, sensor))



f1 = IPhone("7s", "iOS", 64, 32)
f1.info_iphone()
f1.features("Yes", "No", 64, "Yes")

x = f1.displaymsg("EMERGENCY CONTACT: 0303-EMERGENCY")
print(x)

f2 = Samsung("S10", "iOS", 64, 48)
f2.info_samsung()
f2.features("Yes", "Yes", 64, "Yes")

y = f1.displaymsg("I lost my phone. Now I'm broke.")
print(y)

