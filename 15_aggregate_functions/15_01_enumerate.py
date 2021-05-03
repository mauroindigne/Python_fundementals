'''
Demonstrate the use of the .enumerate() function.
'''

motorbikes = ['kawasaki', 'honda', 'yamaha', 'ducati', 'bmw']


def my_enumerate(item, starting_number):
    for index, motorbike in enumerate(item, starting_number):
        print(f"{index}: {motorbike.upper()} ")


my_enumerate(motorbikes, 10)

for index, motorbike in enumerate(motorbikes):
    print(f"{index}: {motorbike.upper()} ")