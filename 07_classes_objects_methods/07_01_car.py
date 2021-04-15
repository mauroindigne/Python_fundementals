'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Car:

    def __init__(self, model, year, speed=0):
        self.model = model
        self.year = year
        self.speed = speed

    def giving_it_gas(self):
        self.speed += 5

    def info(self):
        print(f"This cars model is a {self.model}, and it was produced in {self.year} and it boasts a top speed of {self.speed}")


new_car = Car("Honda NSX", "1995", 150)

new_car.giving_it_gas()

new_car.info()




