'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

word = input("enter a string")
d = {}
for letter in word:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1

print(d)