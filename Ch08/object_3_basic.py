# 딕셔너리 return 함수 선언
def student_create(name, Korean, math, english, science):
    return {
        "name" : name,
        "Korean" : Korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

# 점수 총합 처리하는 함수 선언
def student_get_sum(student):
    return student["Korean"] + student["math"] + student["english"] + student["science"]

# 평균 구하는 함수 선언
def student_get_avg(student):
    return student_get_sum(student) / 4

# 마지막 출력값 return하는 함수 선언
def student_to_string(student):
    return f'{student["name"]}, {student_get_sum(student)}, {student_get_avg(student)}'

# 학생 리스트 선언
students = [
student_create("윤인성", 87, 96, 88, 95),
student_create("강민우", 37, 32, 58, 85),
student_create("박세히", 85, 74, 98, 75),
student_create("가나다", 81, 93, 8, 5)
]


print("이름, 총점, 평균", sep="\t")
    
# 반복하기:

for student in students:
    print(student_to_string(student))