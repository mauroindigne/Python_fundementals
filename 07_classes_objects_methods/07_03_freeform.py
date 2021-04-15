'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''


class WashingMachine:
    def __init__(self, power, loaded, detergent):
        self.power = power
        self.loaded = loaded
        self.detergent = detergent

    def __str__(self):
        if self.power == 'on' and self.loaded == 'loaded' and self.detergent == 'filled':
            return f'The washing machine is {self.power}, {self.loaded} with clothes and {self.detergent} with detergent'
        elif self.power == 'on' and self.loaded == 'loaded' and self.detergent == 'not filled':
            return f'The washing machine is {self.power}, {self.loaded} with clothes but not {self.detergent} with detergent'
        elif self.power == "off":
            return f'The washing machine is {self.power}'
        else:
            return f'the washing machine is either not loaded with detergent or not loaded with clothes'

# --------------------------------------------------------------------------------------------------------------


class Car:
    def __init__(self, model, color, power):
        self.model = model
        self.color = color
        self.power = power

    def powerboost(self):
        if self.color == "red":
            self.power += 50

    def __str__(self):
        return f"The {self.model} is a good car when it comes in {self.color}, because this color gives it {self.power}HP"

# --------------------------------------------------------------------------------------------------------------


class Tree:
    def __init__(self, leaves, color, height=0):
        self.leaves = leaves
        self.color = color
        self.height = height

    def living(self):
        if self.leaves == "yes":
            print("The tree is alive")
        else:
            print("the tree is either dead or its winter")

    def __str__(self):
        if self.leaves == "yes":
            return f'The tree has leaves is {self.color} and has a height of {self.height} meters tall'
        else:
            return f'the tree has no leaves and is {self.color} and has a height of {self.height} meters tall'
# --------------------------------------------------------------------------------------------------------------


print("-----------------------------------------------------------------------------------------\nWashingMachine Class")
# Washing machine
ready_laundry = WashingMachine('on', 'loaded', 'filled')
not_ready_laundry = WashingMachine('off', 'loaded', 'not filled')
not_ready_laundry1 = WashingMachine('on', 'loaded', 'not filled')

print(ready_laundry)
print(not_ready_laundry)
print(not_ready_laundry1)

print("----------------------------------------------------------------------------------------\nCar Class")
# Car
car1 = Car('BMW M5', 'red', 850)
car2 = Car('Ford Ranger', 'Gun metal Gray', 250)
car3 = Car('Nissan Skyline R34', 'midnight purple', 645)

car1.powerboost()
car2.powerboost()
car3.powerboost()

print(car1)
print(car2)
print(car3)

print("----------------------------------------------------------------------------------------\nTree Class")
# Tree
tree1 = Tree('yes', 'Orange', 30)
tree2 = Tree('no', 'brown', 15)

print(tree1)
print(tree2)

