'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

while True:
    try:
        x = int(input("enter a first digit: "))
        y = int(input("enter second digit: "))
        result = x / y
        print(result)
    except ZeroDivisionError:
        print(f"Oi you cant divide a {x} by {y}")
    except ValueError:
        print("The input you gave is a sting not a number...")
