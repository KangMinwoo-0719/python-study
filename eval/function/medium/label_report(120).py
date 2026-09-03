parts = input().split()
label = parts[0]
scores = [int(x) for x in parts[1:]]

def report(label, *scores):
    """
    라벨(label), 점수(scores)를 입력받아
    "{label}: {sum(scores)}" 형식의 문자열을 반환하는 함수
    """

    # label: scores의 합 반환
    return f"{label}: {sum(scores)}"

# ↓ 호출부 (수정하지 마세요) — label 은 위치 인자, 나머지는 * 로 풀어 전달
print(report(label, *scores))