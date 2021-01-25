''' Programming Exercises:

1.Write a program to show classes of umbrella 
and provide the polymorphism mechanism in
umbrella open(), close(), waterproof().

'''

class Umbrella:
    
    def __init__(self, color, size):
        self.color = color
        self.size = size
        
    def set_color(self, color):
        self.color = color
        
    def get_color(self):
        return f"The color of this umbrella is {self.color}"
    
    def set_size(self, size):
        #Small(S), Large(L), Extra Large(XL)
        self.size = size
        
    def get_size(self):
        return f"The size of this umbrella is {self.size}"
    
class parasol(Umbrella):
        
    def Open(self):
        print("Its sunny outside!\nParasol Opened.\n")
        
    
    def Close(self):
        print("Finally some shade.\nParasol closed.\n")
        
    
    def Waterproof(self):
        print("Parasols are not waterproof!\n")

class bumbershoot(Umbrella):
    
    def Open(self):
        print("Its raining outside!\nBumbershoot Opened.\n")

    def Close(self):
        print("Finally the rain stopped.\nBumbershoot closed.\n")
        
    def Waterproof(self):
        print("Bumbershoots are waterproof!\n")
        
class brolly(Umbrella):
    
    def Open(self):
        print("I need a flash.\nBrolly opened.\n")
    
    def Close(self):
        print("Finally the shoot is over.\nBrolly closed.\n")
        
    def Waterproof(self):
        print("Brollies are waterproof!")
        
u1 = parasol("Pink", "S")
u2 = bumbershoot("Blue", "L")
u3 = brolly("Black", "XL")
'''
for things in (u1,u2,u3):
    things.Open()
    things.Close()
    things.Waterproof()
'''

'''
2. Design class for classical, and latest mobiles. 
Use polymorphism to show the functions of these
mobiles such as button() or touch(), size(),
split_screen(), operating_system(). Etc.

'''

class classical_phones:
    
    def button(self):
        print("Classical phones have a buttons for keypad, navigation and power.\n")
        
    def touch(self):
        print("Classical phones do not have touch screens.\n")
        
    def size(self):
        print("Classical phones are small but wide in size.\n")
        
    def split_screen(self):
        print("Classical phones do not have split screens.\n")
        
    def operating_system(self):
        print("Classical phones either had 'Series 20' or 'iPhone OS 1.0' as their operating system.\n")
class latest_phones:
    
    def button(self):
        print("Latest phones have a buttons for volume and power.\n")
        
    def touch(self):
        print("Latest phones have touch screens.\n")
        
    def size(self):
        print("Latest phones are compact and slim in size.\n")
        
    def split_screen(self):
        print("Latest phones have split screens in exceptional models.\n")
        
    def operating_system(self):
        print("Latest phones either have 'Android' or 'iOS' as their operating system.\n")    

p1 = classical_phones()
p2 = latest_phones()

def description(info):
    info.button()
    info.touch()
    info.size()
    info.split_screen()
    info.operating_system()

#description(p1)
#description(p2)


'''
3. Design class for Butterfly. 
Such that butterfly has multiple colors, patters, 
nature of living, origin,
living_in_pupa, living_as_caterpiller. Etc.

'''

class Butterfly:
    
    def __init__(self, color, patterns, origin, caterpillarlife, pupalife):
        self.color = color
        self.patterns = patterns
        self.origin = origin
        self.caterpillarlife = caterpillarlife
        self.pupalife = pupalife
        

class Nymphalidae(Butterfly):
    
    def __init__(self, name):
        super().__init__("High contrast, Red/Blue,Black,Orange", "Pairs of colors in Patches", "North America", 5, 7)
        self.name = name

    def info(self):
        print(f"{self.name},\nColor: {self.color}\nPatterns: {self.patterns}\nOrigin: {self.origin}\n")
    
    def lifespan(self):
        print(f"{self.name},\nLife as Caterpillar: {self.caterpillarlife} days\nLife as Pupa: {self.pupalife} days\n")

class Hedylidae(Butterfly):
    
    def __init__(self, name):
        super().__init__("Dull Wooden", "Brushed", "Mexico", 10, 7)
        self.name = name

    def info(self):
        print(f"{self.name},\nColor: {self.color}\nPatterns: {self.patterns}\nOrigin: {self.origin}\n")
    
    def lifespan(self):
        print(f"{self.name},\nLife as Caterpillar: {self.caterpillarlife} days\nLife as Pupa: {self.pupalife} days\n")

b1 = Nymphalidae("Brush-footed Butterfly")
b2 = Hedylidae("American moth-Butterfly")

def details(x):
    x.info()
    x.lifespan()

#details(b1)
#details(b2)

