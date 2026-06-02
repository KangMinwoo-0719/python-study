data_sets = [
    {
        "윤서": {"수학": 85, "영어": 90, "과학": 78},
        "지우": {"수학": 92, "영어": 88, "과학": 95},
        "민준": {"수학": 65, "영어": 70, "과학": 80},
    },
    {
        "A": {"수학": 90, "영어": 80},
        "B": {"수학": 70, "영어": 80},
    },
    {
        "혼자": {"수학": 80},
    },
]
t = int(input())
students = data_sets[t]
student_average = 0
average_total = 0

# 현재 딕셔너리의 value(dict)의 value값 평균 구하여 출력
for name, dicts in students.items():
    student_average = sum(dicts.values()) / len(dicts)
    print(f"{name}: {student_average:.1f}")
    
    # 학생 평균값 누적
    average_total += student_average

# 전체 평균값 출력
print(f"전체 평균: {average_total / len(students):.1f}")