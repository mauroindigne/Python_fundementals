'''
Write a script that takes a tuple and turns it into a list.

'''

tuples = [(1, 2), (3, 4), (5, 6)]
lists = [list(x) for x in tuples]
print(lists)
