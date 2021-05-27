'''
Exercise 3: Write a program to prompt the user for hours and rate per
hour to compute gross pay.
'''
hours = int(input("How many hours do you work mate? \n"))
rate = float(input("and how much they pay for an hour? \n"))
gross_pay = hours * rate
print(f"So you must make {gross_pay} a week!")
