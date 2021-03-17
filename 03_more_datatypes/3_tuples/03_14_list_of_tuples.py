'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
result_list = []
sentence = input("enter any string here:")
words = sentence.split(" ")

for word in words:
    result_list.append(tuple(word))

print(result_list)
