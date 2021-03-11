'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

num = int(input("Type in any int"))
# 1
print(float(num))


# 2
print(int(num))

# 3
floor = 2.5 // 5
print(floor)

# 4
first = int(input("type in a number:"))
second = int(input("type in another number:"))
print(first * second)
