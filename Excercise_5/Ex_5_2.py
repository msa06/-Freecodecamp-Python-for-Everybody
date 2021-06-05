'''
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average
'''
numbers = []
while True:
    try:
        userinput = input("Enter a number: ")
        if userinput == "done":
            break
        num = int(userinput)
        numbers.append(num)
    except:
        print("Invalid Input")
        pass
total = 0
max = None
min = None
for itervar in numbers:
    total += itervar
    if max is None or itervar > max:
        max = itervar
    if min is None or itervar < min:
        min = itervar

print(f"Total:{total}")
print(f"Maximum :{max}")
print(f"Minimum:{min}")
