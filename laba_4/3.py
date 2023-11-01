class Pet_shop:
    
    def __init__(self):
        print("Pet shop")
        
class Animal:
    
    def __init__(self,breed,cost):
        self.breed = breed
        self.cost = cost
        
    def movement(self):
        print("I'm moving")
        
class Fish(Animal):
    
    def movement(self):
        print("I'm swimming")
        
class Bird(Animal):
    
    def movement(self):
        print("I'm flying")
        
        
        