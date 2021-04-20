'''
Write a script that demonstrates a try/except/else.

'''

while True:
    try:
        x = int(input("enter a first digit: "))
        y = int(input("enter second digit: "))
        result = x / y
    except ZeroDivisionError:
        print(f"Oi you cant divide a {x} by {y}")
    else:
        print(result)