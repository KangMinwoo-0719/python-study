scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 현재 딕셔너리의 평균 값 구하기
scores_avg = sum(scores.values()) / len(scores)

# 현재 딕셔너리에서 점수 추출 후 정렬
scores_sorted = sorted([score for score in scores.values()], reverse=True)

# 해당 학생 이름이 딕셔너리에 없다면 학생 없음 출력
if name not in scores:
    print("학생 없음")

# 있는 경우:
else:

    # 이름, 점수 출력
    print(f"이름: {name}")
    print(f"점수: {scores[name]}")

    # abs(평균 - 점수) 후 평균보다 크면 +, 작으면 - 붙인 후 차이 출력
    mark = "+" if scores[name] > scores_avg else "-"
    print(f"평균 차이: {mark}{abs(scores_avg - scores[name])}")

    # 등수 출력
    print(f"등수: {scores_sorted.index(scores[name]) + 1}등")