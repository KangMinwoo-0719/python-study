opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

def merge_to_string(**kwargs):
    """
    kwargs 인자를 받아
    key 사전순으로 정렬한 후 "," 를 기준으로 구분하여
    key=value 형식의 문자열을 반환하는 함수
    """

    # key 순서로 정렬 후 ","를 기준으로 구분한 문자열 반환
    return ",".join(sorted(f"{key}={value}" for key, value in kwargs.items()))
    

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(merge_to_string(**opts))