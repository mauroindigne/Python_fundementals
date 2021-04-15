'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''


class Planet():

    def __init__(self, name, color, system):
        self.name = name
        self.color = color
        self.system = system

    def __str__(self):
        return f"Planet {self.name} is {self.color} planet in the {self.system}"

    def bears_life(self):
        if self.color.lower() == 'blue':
            return True
        else:
            return False


mars = Planet('Mars', 'red', 'Solar System')
earth = Planet('Earth', 'blue', 'Solar System')

print(mars)
