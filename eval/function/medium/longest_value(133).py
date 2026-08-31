opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

def longest_value(**opts):
    """
    문자열을 받아 길이가 가장 긴 문자열의
    value를 반환하는 함수
    """
    # 길이가 가장 긴 문자열을 가진 key를 저장할 변수
    longest_val = ''

    # opts 딕셔너리를 순회하여 길이가 가장 긴 key값 return
    for val in opts.values():
        if len(val) > len(longest_val):
            longest_val = val 

    return longest_val

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(longest_value(**opts))