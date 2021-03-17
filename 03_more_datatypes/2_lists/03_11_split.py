'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

sentence = input("enter any string here:")
words = sentence.split(" ")


def most_frequent(words):
    counter = 0
    num = words[0]

    for i in words:
        curr_frequency = words.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num

print("the most common word used was:", most_frequent(words))
