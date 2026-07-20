names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["X", "Y"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 해당 점수 집합의 평균 구하기
avg = sum(scores) / len(scores)

# 가장 근접한 학생의 이름, 점수를 저장할 변수
best_name = ''
best_score = -1
best_diff = float('inf')

# 이름과 점수 집합 동시 순회:
for name, score in zip(names, scores):

    # 현재 학생의 평균 차 저장
    diff = abs(avg - score)

    # 평균 - 학생 점수가 이전 값보다 작으면 이름과 점수 갱신
    if diff < best_diff:
        best_name = name
        best_score = score
        best_diff = diff

# 이름: 점수 형식 출력
print(f"{best_name}: {best_score}")