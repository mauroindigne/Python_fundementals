'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
game = True

number = int(input("pick any number between 1 and 1,000,000,000 to see if its divisible by 3:"))
while game:
    if number % 3 == 0:
        print(number, "is divisible by 3")
        break
    else:
        print(number, "is not divisible by 3")
        break
