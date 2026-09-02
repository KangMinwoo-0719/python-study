opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

def average_values(**kwargs):
    """
    kwargs 인자값들의 평균 값을 반환하는 함수
    """

    # 인자값의 평균값을 반환하기
    return sum(kwargs.values()) // len(kwargs)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(average_values(**opts))