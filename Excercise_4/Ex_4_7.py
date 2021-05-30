'''
Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
'''


def computeGrade(score):
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"


score = 0
while True:
    try:
        score = float(input("Enter Your Score (0 - 1): "))
        if score > 1 or score < 0:
            print("Please Enter the Score in right range!!")
        else:
            break
    except:
        print("Bad Score")

grade = computeGrade(score)
print(f"You Score: {grade}")
