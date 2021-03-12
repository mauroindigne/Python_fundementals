'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

first = input("enter any word here:")
second = input("enter any word here:")
third = input("enter any word here:")

print(len(first), ":", first)
print(len(second), ":", second)
print(len(third), ":", third)