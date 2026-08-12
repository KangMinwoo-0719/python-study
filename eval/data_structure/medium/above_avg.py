# 평균 변수 한 번 계산 후 두 그룹 list 에 분류.
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
avg_over = []
avg_under = []

# 해당 그룹의 점수 평균 구하기
std_avg = sum(scores) / len(scores)

# 해당 그룹의 학생 이름, 점수 동시 순회:
for name, score in zip(names, scores):

    # 해당 학생의 점수가 평균보다 크면(이상) 평균 이상 그룹에 추가
    if score >= std_avg:
        avg_over.append(name)

    # 낮은 경우는 평균 이외의 그룹에 저장
    else:
        avg_under.append(name)

# 평균 이상, 미만 그룹 명단 출력
print(f"평균 이상: {' '.join(avg_over)}")
print(f"평균 미만: {' '.join(avg_under)}")