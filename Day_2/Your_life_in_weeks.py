age = input("What is your current age? ")

years_left = 30 - int(age)
months_keft = 12 * years_left
weeks_left = 52 * years_left
days_left = years_left * 365 

message = f"You have {days_left} days, {weeks_left} weeks, and {months_keft} months left."
print(message)