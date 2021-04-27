'''
Write a script with a function that demonstrates the use of **kwargs.

'''

names = []

def my_function(**kwargs):
    for k, v in kwargs.items():
        names.append(v)
        print(f'{k}: {v.capitalize()}')


my_function(name1='john', name2='steven', name3='bob', name4='jerry')

print(f'list if names: {names}')
