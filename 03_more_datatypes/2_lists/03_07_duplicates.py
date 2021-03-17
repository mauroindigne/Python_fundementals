'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

clean = []
for i in list_:
    if i not in clean:
        clean.append(i)
print(clean)

# what a set is in python
