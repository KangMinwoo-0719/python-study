data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [3, 1, 2],
    [50],
]
t = int(input())
scores = data_sets[t]

# 현재 list의 결과 내림차순 정렬로 출력
print(*sorted(scores, reverse = True))