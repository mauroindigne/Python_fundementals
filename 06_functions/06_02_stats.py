'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]


def stats(a):
    # maximum value
    maximum = max(a)
    print(maximum)
    # minimum value
    minimum = min(a)
    print(minimum)
    # average value
    average = sum(a) / len(a)
    print(average)
    # sum value
    total = sum(a)
    print(total)


# call the function below here
print(stats(example_list))