'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
import random

numbers = []
try:
    with open("integers.txt", "r") as bic:
        for number in bic.readlines():
            number = number.rstrip()
            numbers.append(int(number))
except IOError:
    print("It seems I couldnt accese the file your looking to open")
except ValueError:
    print("There is a str or float in the integers.txt file, but it wont be added to the numbers list")

print(numbers)

try:
    x = random.choice(numbers)
    y = random.choice(numbers)
    result = x / y
    print(f"We take two random value from integers.txt. Next we assign them to a variable like this X = {x} and Y = {y}\nlets divide X by Y and we get {result}")
except ValueError:
    print("Naa that doesnt work")
except ZeroDivisionError:
    print("The Value of 0 was chosen for Y, but you cant divide a number by 0")
# there is no items in the integers.txt file
except IndexError:
    print("It seems that there are no items in the list numbers")
