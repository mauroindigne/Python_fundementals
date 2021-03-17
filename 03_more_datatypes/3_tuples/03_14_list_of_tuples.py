'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
result_list = []
sentence = input("enter any string here:")
words = sentence.split(" ")
letters = words.split("")
result_list.append(letters)
print(letters)