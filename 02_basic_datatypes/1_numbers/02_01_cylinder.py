'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.

'''

h = 5
r = 3.14
pie = 3.14159265359
volume = (pie * (r ** 2) * h)
surface = ((2 * pie * r * h) + (2 * pie * (r ** 2)))
print(volume)
print(surface)