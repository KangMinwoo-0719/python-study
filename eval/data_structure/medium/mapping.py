names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["혼자"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [100, 55, 72],
    [85],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 이름과 등급을 저장하는 딕셔너리 매핑
students_dict = {
    name : ('A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F')
    for name, score in zip(names, scores)
}


# 딕셔너리를 순회하며 이름, 등급 출력
for name, grade in students_dict.items():
    print(f"{name}: {grade}")