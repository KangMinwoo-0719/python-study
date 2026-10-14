def evaluate(score):

    """
    점수(score)를 입력받아 0 미만 100 초과인 경우 즉시 종료,
    0 이상 100 이하인 경우 60 이상은 "합격", 60 미만은 "불합격"을 반환하는 함수
    """

    # score가 0 미만, 100 초과인 경우 "유효하지 않음" 반환
    if score < 0 or score > 100:
        return "유효하지 않음"

    # 60점 이상인 경우 "합격", 미만인 경우 "불합격" 반환
    return "합격" if score >= 60 else "불합격"

# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "85" 이면 score == 85
score = int(input())

# 함수 호출 후 반환값 출력
print(evaluate(score))