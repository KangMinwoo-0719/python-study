scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 딕셔너리 value 평균 계산
avg = sum(scores.values()) // len(scores)

# 입력받은 이름(key)의 점수(value) 접근하여 평균 - 점수 계산 절대값 출력
print(f"차이: {abs(avg - scores[name]):.1f}")