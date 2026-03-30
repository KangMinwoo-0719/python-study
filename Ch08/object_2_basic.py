# 딕셔너리 리턴 함수 선언
def student_create(name, Korean, math, english, science):
    return {
        "name" : name,
        "Korean" : Korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

# 학생 리스트 선언
students = [
student_create("윤인성", 87, 96, 88, 95),
student_create("강민우", 37, 32, 58, 85),
student_create("박세히", 85, 74, 98, 75),
student_create("가나다", 81, 93, 8, 5)

]

print("이름, 총점, 평균", sep="\t")

# 학생 한 명씩 반복하기:
for student in students:

    # 점수 총합과 평균 구하기
    score_sum = student["Korean"] + student["math"] + student["english"] + student["science"]

    score_avg = score_sum / 4


    # 출력하기
    print(f'{student["name"]}, {score_sum}, {score_avg}')