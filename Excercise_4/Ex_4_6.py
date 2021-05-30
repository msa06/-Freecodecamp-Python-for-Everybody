'''
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''


def computepay(hours, rate):
    if hours > 40:
        diff = hours - 40  # 5
        newrate = rate * 2.5  # 10*2.5 = 25
        overtime = diff * newrate  # 125
        return 40 * rate + overtime  # 400 + 125
    else:
        return hours * rate


hours = int(input("How many hours do you work mate? \n"))
rate = float(input("and how much they pay for an hour? \n"))
overtime = 0
gross_pay = 0
gross_pay = computepay(hours, rate)

print(f"So you must make {gross_pay} a week!")
