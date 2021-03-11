'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
amount = int(input("how much are you going to invest"))
intrest = float(input("whats the interest rate in percentage"))
years = int(input("how many number of years to invest"))

print((amount * intrest) * years)