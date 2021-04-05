'''
Write a script that "flattens" a shallow list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

Note that your input list only contains one level of nested lists.
This is called a "shallow list".

CHALLENGE: Do some research online and find a solution that works
to flatten a list of any depth. Can you understand the code used?

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

# make new list to appened items into
flatten_list = []

# for loop to take all items in list
for l in starting_list:

    # take each item that we called L and append it into the flattened_list
    for item in l:

        flatten_list.append(item)

print(flatten_list)