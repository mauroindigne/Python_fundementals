'''
Write a lambda function that takes in 3 numbers and returns the sum of the numbers.

'''

three_numbers = lambda x, y, z: x + y + z

first = int(input("enter first number: "))

second = int(input("enter second number: "))

third = int(input("enter third number: "))

print(three_numbers(first, second, third))