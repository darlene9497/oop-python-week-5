class Cheetah:
    def move(self):
        return "Sprinting 🐆"

class Car:
    def move(self):
        return "Driving 🚗" 

class Plane:
    def move(self):
        return "Flying ✈️" 

# polymorphism
for objects in [Cheetah(), Car(), Plane()]:
    print(objects.move())