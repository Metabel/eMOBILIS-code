#car:brand,color,horsepower
class Car:
    def __init__(self,color,brand,horsepower):
        self.color =color
        self.brand =brand
        self.horsepower=horsepower
        
    def display_info(self):
        return f"This car is {self.color} {self.brand} with a horsepower of {self.horsepower}"
#create an object
car1=Car("yellow","bmw","1200") 
car2=Car("white","Mercedes","1500")
print(car1.display_info())
print(car2.display_info())
print(car1.brand)
print(car1.color)
print(car1.horsepower)
        
          