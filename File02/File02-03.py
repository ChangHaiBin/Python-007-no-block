
# Make sure to cover all edge cases!
# Missing "else" case!
def get_exam_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"

score1 = 85
grade1 = get_exam_grade(score1)
print(grade1)

score2 = 47
grade2 = get_exam_grade(score2)
print(grade2)

score3 = 29
grade3 = get_exam_grade(score3)
print(grade3)
