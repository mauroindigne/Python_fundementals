'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

with open("books/war_and_peace.txt", "r") as wap:
    book1 = wap.read()

with open("books/crime_and_punishment.txt", "w") as cap:
    book2 = cap.write("")

with open("books/pride_and_prejudice.txt", "r") as pap:
    book3 = pap.read()

for item in book1, book2, book3:
    try:
        print(f"The first character is {item[0]}")
    except TypeError:
        print(f"Theres no items in {item}")




