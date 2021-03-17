'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

print("we need you to enter a total of 10 numbers")
enter = True
count = 0
digits = []
while enter:
    if count < 10:
        choices = int(input("Enter a number:"))
        digits.append(choices)
        count += 1
    else:
        break

print("the largest number in the list is:", max(digits))





