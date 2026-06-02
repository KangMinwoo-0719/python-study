# 점수가 동률인 경우 이름 알파벳순으로 자동 정렬됨.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"A": 50, "B": 50, "C": 50},
]
t = int(input())
scores = data_sets[t]

# tuple로 값 저장 후 전체 정렬
scores_sorted_paris = sorted((score, name) for name, score in scores.items())

# 정렬된 튜플 순회하며 출력
for score, name in scores_sorted_paris:
    print(f"{name}: {score}")