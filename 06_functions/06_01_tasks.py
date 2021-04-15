'''

Write a script that completes the following tasks.

'''


# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def challenge1(a):
    if a % 4 == 0 or a % 7 == 0:
        return True
    return False


print(challenge1(4))


# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def challenge2(a):
    if a % 4 == 0 and a % 7 == 0:
        return True
    return False


print(challenge2(9))

# take in a number from the user between 1 and 1,000,000,000
# call your functions, passing in the user input as the arguments, and set their output equal to new variables
# print your new variables to display the results
user_input = int(input("Pick any number between 1 and 1,000,000,000: "))
print(challenge1(user_input))
print(challenge2(user_input))


