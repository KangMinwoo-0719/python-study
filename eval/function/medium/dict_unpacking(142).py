opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def box(width, height):
    return width + "x" + height

# 함수 호출 후 반환값 출력
print(box(**opts))