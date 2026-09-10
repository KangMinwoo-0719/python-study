opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def collect(**kwargs):
    return ",".join(sorted(kwargs))

# 함수 호출 후 딕셔너리(opts) 언패킹한 값 넘긴 후 반환값 출력
print(collect(**opts))