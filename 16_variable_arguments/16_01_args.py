'''
Write a script with a function that demonstrates the use of *args.

'''

def my_function(*args):
    for i in args:
        print(f"{i.capitalize()}s")

my_function('bird', 'dog', "cow", 'horse')

