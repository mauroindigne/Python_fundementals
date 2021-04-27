'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

cars = [3, 5, 53, 34]

def my_enumerate(x):
    for y in range(len(x)):
        print(f"lot #{y} has {x[y]} Cars")

my_enumerate(cars)