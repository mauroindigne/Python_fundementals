'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
words = []

with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)

# Shortests words
min_len = len(min(words, key=len))
print("The shortest word('s): ",[word for word in words if len(word) == min_len])

# Longest
max_len = len(max(words, key=len))
print("The longest word('s): ",[word for word in words if len(word) == max_len])

number_of_words = len(words)
print(f"the total number of words is {number_of_words}")