# 학생 리스트 선언
students = [
    {"name" : "윤인성", "Korean" : 87, "math" : 98, "english" : 88, "science" : 91},
    {"name" : "연하진", "Korean" : 92, "math" : 94, "english" : 80, "science" : 45},
    {"name" : "구지연", "Korean" : 76, "math" : 91, "english" : 54, "science" : 95},
    {"name" : "나선주", "Korean" : 100, "math" : 88, "english" : 28, "science" : 98},
    {"name" : "윤아린", "Korean" : 80, "math" : 91, "english" : 86, "science" : 97},
    {"name" : "윤명월", "Korean" : 63, "math" : 80, "english" : 70, "science" : 54}
]

# sep = "\t" : 출력 인자값 사이를 tab 으로 구분
print("이름", "총점", "평균", sep="\t")

# 학생 한 명씩 반복p
for student in students:

# 점수 총합과 평점 구하기
    score_sum = student["Korean"] + student['math'] + student["english"] + student["science"]

    score_avg = score_sum / 4


    # 출력하기
    print(f'{student["name"]}, {score_sum}, {score_avg}', sep="\t")