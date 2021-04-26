'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

gen = (i for i in range(15))
print(gen)

for i in gen:
    if i % 2 == 0:
        print(i)