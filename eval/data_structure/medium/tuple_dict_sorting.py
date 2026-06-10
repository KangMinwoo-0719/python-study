data_sets = [
    [(85, "윤서"), (92, "지우"), (65, "민준"), (78, "서윤"), (95, "도윤")],
    [(80, "A"), (70, "B"), (90, "C")],
    [(50, "혼자")],
]
t = int(input())
students = data_sets[t]

# 현재 리스트 점수 정렬 후 순회:
for score, name in sorted(students):

    # 이름: 점수 형식 출력
    print(f"{name}: {score}")