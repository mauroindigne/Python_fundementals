'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''
number = 0
digits = []
while number < 1000:
    number += 5
    digits.append(number)
print(digits)