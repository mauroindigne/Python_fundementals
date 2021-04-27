'''
Demonstrate the use of the .enumerate() function.
'''

motorbikes = ['kawasaki', 'honda', 'yamaha', 'ducati', 'bmw']


def my_enumerate(item, index):
    for x, y in enumerate(item, index):
        print(f"{x}: {y.upper()} ")


my_enumerate(motorbikes, 1)

