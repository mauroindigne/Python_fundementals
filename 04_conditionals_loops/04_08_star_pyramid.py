'''
Write a script that takes in a number from the user as input and prints the following structure.

Suppose the input is 5, you will output
*
* *
* * * 
* * * *
* * * * * 
i.e. number of rows will be 5, 1st row will have 1 star, 2nd row will have 2 stars, 3rd row 3 stars, 4th row will have 4 stars and 5th row will have 5 stars.

Another example: if input is 3, you will output
*
* *
* * *

Hint: Think of nested for loops

'''

n = int(input("enter any number:"))
# outer loop to handle number of rows
for i in range(0, n):
    # inner loop to handle number of columns
    # values is changing according to outer loop
    for j in range(0, i + 1):
        # printing stars
        print("* h ", end="")

        # ending line after each row
    print()
