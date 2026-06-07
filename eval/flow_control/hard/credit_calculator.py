n = int(input())
total_credit = 0
current_score = float(0)
total_grade_score = 0

# n값 범위 반복:
for num in range(1, n + 1):

    # 등급과 이수학점 공백으로 나누어 입력받기
    grade, credit = input().split()

    # 현재 과목 순번과 학점 출력
    print(f"과목{num}: {grade} ({credit}학점)")

    # 학점 누적하기
    total_credit += int(credit)

    # A+ ~ F 범위에 맞게 학점 부여
    if grade == "A+":
        current_score = 4.5
    elif grade == "A":
        current_score = 4.0
    elif grade == "B+":
        current_score = 3.5
    elif grade == "B":
        current_score = 3.0
    elif grade == "C+":
        current_score = 2.5
    elif grade == "C":
        current_score = 2.0
    elif grade == "D+":
        current_score = 1.5
    elif grade == "D":
        current_score = 1.0
    elif grade == "F":
        current_score = 0.0

    # 해당 과목 학점점수 * 이수학점 계산 후 누적
    total_grade_score += current_score * int(credit)

# GPA 계산 후 출력
gpa = total_grade_score / total_credit
print(f"GPA: {gpa:.2f}")