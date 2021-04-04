'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''

j = 0
count = -1
# outer loop to handle number of rows
for i in range(0, 5):
    # inner loop to handle number of columns
    for j in range(0, 10):
        # values is counted up by 1 each time
        count += 1
        print(count, " ", end="")
        # print count then add space and at end of list start new line
    print()