'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5
# outer loop to handle number of rows
for i in range(0, n):
    # inner loop to handle number of columns
    # values is changing according to outer loop
    for j in range(0, i + 1):
        # printing stars
        print("* ", end="")

        # ending line after each row
    print()