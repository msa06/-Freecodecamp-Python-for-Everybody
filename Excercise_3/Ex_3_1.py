'''
Exercise 1: Rewrite your pay computation to give the employee 1.5
times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

'''
hours = int(input("How many hours do you work mate? \n"))
rate = float(input("and how much they pay for an hour? \n"))
overtime = 0
gross_pay = 0
if hours > 40:
    diff = hours - 40
    newrate = rate * 1.5
    overtime = diff * newrate
    gross_pay = 40 * rate + overtime
else:
    gross_pay = hours * rate


print(f"So you must make {gross_pay} a week!")
