"""Question 2
Perform the following task:
    1. Create a class dinner having dishes inside the dinner class such as 
    soup, salad, course, dessert and juice.
    2. Create methods that can print these dishes inside the dinner such as
    soup, salad, course, dessert and juice.
    3. Create objets of your friends and change the parameters according to
    each friend.
    
"""
class dinner:
    
    def __init__(self, app, meal, dessert, juice):
        self.app = app
        self.meal = meal
        self.dessert = dessert
        self.juice = juice
        
    def course(self):
        print("This 3 course meal consists of a warm serving of {} following with {} and {}, complementary {} in dessert.".format(self.app,
                                                                            self.meal, self.juice, self.dessert))

me = dinner("Shrimp Soup", "Szechaun Chicken", "Quesillo", "Mint Lemonade")
me.course()

p1 = dinner("Mashed Potatoes", "Beef Steak", "Mousse", "Margarita")
p1.course()

p2 = dinner("Garlic Bread", "Penne", "Cheesecake", "Grape Juice")
p2.course()

















