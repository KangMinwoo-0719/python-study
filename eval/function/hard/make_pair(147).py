tokens = input().split()
pair = tokens[:2]
opts = {}
for token in tokens[2:]:
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def make(a, b, sep="-", end="!"):
    return a + sep + b + end


# make 함수 호출 후 pair, opts 인자를 언패킹하여 넘겨주기
# 이후 반환된 값 출력
print(make(*pair, **opts))