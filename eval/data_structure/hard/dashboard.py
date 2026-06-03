data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95, "예준": 50},
    {"A": 80, "B": 62, "C": 90, "D": 55},
    {"혼자": 100},
]
t = int(input())
scores = data_sets[t]

# 해당 딕셔너리의 점수 합 / 길이 -> 평균 1의 자리까지 구하기
students_avg = sum(scores.values()) / len(scores)
print(f"전체 평균: {students_avg:.1f}")

# 최고점 value의 key(이름)와 점수 출력
top_score = max(scores.values())
top_student = [name for name, score in scores.items() if score == top_score]
print("최고점:", *top_student, "(" + str(top_score) + ")")

# 최저점 이름과 점수 출력
low_score = min(scores.values())
low_student = [name for name, score in scores.items() if score == low_score]
print("최저점:", *low_student, "(" + str(low_score) + ")")

# 60점 이상의 학생들(합격자)을 카운트 후 출력
accepts = sum([1 for accept in scores.values() if accept >= 60])
print(f"합격자: {accepts}명")

# 합격자 / 전체 학생 -> 합격률 1의 자리까지 출력
percentage = accepts / len(scores) * 100
print(f"합격률: {percentage:.1f}%")