'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

words = []

with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)


words_20char = []

for w in words:
    if len(w) > 20:
        words_20char.append(w)

print(words_20char)
