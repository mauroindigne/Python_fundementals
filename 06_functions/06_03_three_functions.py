'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

user_input = int(input("Enter your age: "))


# calculates users age in days
def age_in_days(a):
    days = ((a / 4) + (a * 365))
    return days


# calculates users age in hours
def age_in_hours(a):
    hours = a * 24
    return hours


# calculates users age in seconds
def age_in_seconds(a):
    seconds = (a * 24) * 60 * 60
    return seconds


# Call the age_in_days function with the parameters of the users input
print("You are", age_in_days(user_input), "days old")
# Calls the age_in_hours function with the parameters of the value returned from the age_in_days function
print("You are", age_in_hours(age_in_days(user_input)), "hours old")
# Calls the age_in_seconds function with the parameters of the value returned from the age_in_days function
print("You are", age_in_seconds(age_in_days(user_input)), "seconds old")
