
def get_exam_grade(score):
    if score >= 80:
        return "A"
    else:
        return "B"

score1 = 85
grade1 = get_exam_grade(score1)
print(f"Andy's score is {score1}, and his grade is {grade1}.")

score2 = 73
grade2 = get_exam_grade(score2)
print(f"Brandon's score is {score2}, and his grade is {grade2}.")


