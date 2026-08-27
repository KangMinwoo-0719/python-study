opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

def sum_values(**opts):
    """
    key=value 형식의 opts 인자를 받아
    value 값의 합산을 반환하는 함수
    """

    # opts 딕셔너리에서 values의 합을 반환
    return sum(opts.values())

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(sum_values(**opts))