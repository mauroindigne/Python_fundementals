'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

sentence = input("type any sentence that you want:")
letter = input("enter any 1 letter:")
print(sentence.count(letter))
