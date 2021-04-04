'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

first = int(input("Enter any number:"))
second = int(input("Enter any number again:"))
sum = 0

for i in range(first, second+1):
    sum += i

print("the sum of all the ints between", first, "and", second, "is:", sum)
