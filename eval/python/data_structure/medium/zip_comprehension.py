names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B"],
    ["solo"],
]
scores_sets = [
    [85, 92, 78, 95, 88],
    [100, 200],
    [42],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 각 세트의 인덱스에 대응하게 f string으로 저장 후 출력
print(*[f"{name}={score}" for name, score in zip(names, scores)])