'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}
result = {}

# Extract the unique keys from both dicts
keys = set.union(set(dict_1.keys()), set(dict_2.keys()))

# Initialize the values of the result dictionary
for key in sorted(keys):
    result[key] = 0

# Append the values of dict_1 and dict_2 to result if key is present
for key in keys:
    if key in dict_1:
        result[key] += dict_1[key]

    if key in dict_2:
        result[key] += dict_2[key]

print(result)