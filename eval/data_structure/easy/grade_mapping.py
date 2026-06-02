data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

# 딕셔너리 순회:
for name, score in scores.items():

    # 현재 score가 90 이상이면 A
    if score >= 90:
        grade = 'A'

    # 80 이상이면 B
    elif score >= 80:
        grade = "B"

    # 70 이상이면 C
    elif score >= 70:
        grade = "C"

    # 60 미만이면 D
    elif score >= 60:
        grade = "D"

    # 그 이외 F
    else:
        grade = "F"

    # 변경값 출력
    print(f"{name}: {grade}")