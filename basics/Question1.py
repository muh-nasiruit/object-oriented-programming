"""Question 1
Perform the following task:
    1. Create a class having personal information, hobbies.
    2. Create methods that can print these information and hobbies.
    3. Create objects of your friends and change the parameters 
    according to each friend.

"""
class About:
    
    def __init__(self, name, age, gender, hobbies):
        self.name = name
        self.age = age
        self.gender = gender
        self.hobbies = hobbies
        
    def info(self):
        print("{}, {}{} has a keen interest in {}.".format(self.name, self.age,
                                                           self.gender, self.hobbies))
    
me = About("Mr. Nasir", 20, "M", "programming")
me.info()

f1 = About("Mr. Fasih", 20, "M", "football")
f1.info()

f2 = About("Mr. Zafir", 18, "M", "gaming")
f2.info()

f3 = About("Ms. Ayesha", 19, "F", "badminton")
f3.info()