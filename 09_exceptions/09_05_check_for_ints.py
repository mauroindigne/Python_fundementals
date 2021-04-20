'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

while True:
    try:
        user = int(input("Give me a integer: "))
        print(f"Thanks you gave me an integer and it was {user}")
        break
    except ValueError:
        print("Naa that is in-fact not an integer mate")