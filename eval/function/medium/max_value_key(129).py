opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

def max_value_key(**kwargs):
    """
    kwargs 딕셔너리 인자를 받아
    가장 큰 value 값을 가진 key를 반환하는 함수
    """

    # max값 value를 가진 key를 get으로 가져온 후 return 하기
    return max(kwargs, key=kwargs.get)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(max_value_key(**opts))