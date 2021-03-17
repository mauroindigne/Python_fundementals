'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

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
print(digits)
print(digits[1], digits[3], digits[5], digits[7], digits[9], digits[8], digits[6], digits[4], digits[2], digits[0])

#this one