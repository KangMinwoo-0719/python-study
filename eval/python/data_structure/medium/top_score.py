data_sets = [
    [("윤서", 85), ("지우", 92), ("민준", 65), ("서윤", 78), ("도윤", 95)],
    [("A", 70), ("B", 90), ("C", 80)],
    [("solo", 70)],
]
t = int(input())
students = data_sets[t]
top_score = 0
top_name = ''

# 튜플을 순회하기:
for name, score in students:

    # 현재 값이 이전 값보다 높으면 갱신
    if score > top_score:
        top_score = score
        top_name = name

# 갱신값 출력
print(f"{top_name}: {top_score}")