'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]


def get_unique_list(list_):

    unique_list = []

    unique_numbers = set(list_)

    for list_ in unique_numbers:
        unique_list.append(list_)

    return unique_list


print(get_unique_list(list_))

# do it without set