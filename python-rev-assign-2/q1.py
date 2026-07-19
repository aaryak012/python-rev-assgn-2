#Q1
def student_scores(scores):
    for name, score in scores.items():
        print(f"{name} scored {score}")

scores = {"Aarya": 85, "Esha": 95, "Sanica": 92}
student_scores(scores)
