'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

sentence = input("Enter any sentence that you want:")
vowels = "aeiou"
for v in vowels:
    print(v, sentence.lower().count(v))