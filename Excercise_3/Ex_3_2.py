'''
Exercise 2: Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. The following shows two executions of the
program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input

'''
hours = 0
rate = 0
while True:
    try:
        hours = int(input("How many hours do you work mate? \n"))
        break
    except:
        print("Please Enter numeric input")

while True:
    try:
        rate = float(input("and how much they pay for an hour? \n"))
        break
    except:
        print("Please Enter numeric input")


gross_pay = hours * rate
print(f"So you must make {gross_pay} a week!")
