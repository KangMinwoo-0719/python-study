opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)


def sum_positive_values(**kwargs):
    """
    kwargs 인자를 받아 양수(0 이상)인 value의 총 합을
    반환하는 함수
    """

    # value를 순회하며 양수인 값만 합하여 반환
    return sum(val for val in kwargs.values() if val > 0)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(sum_positive_values(**opts))