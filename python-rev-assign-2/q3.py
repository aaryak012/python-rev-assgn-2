#Q3
def grade_message(score):
    if score >= 90:
         print(f"Great job! You got an A. Your score is {score}.")
    elif 80 <= score <= 89:
        print(f"Good work! You got a B. Your score is {score}.")
    else:
        print(f"Keep practicing! You got a C. Your score is {score}.")

grade_message(92)
grade_message(85)
grade_message(70)

