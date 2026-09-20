parts = input().split()
width = int(parts[0])
height = int(parts[1])
fill = parts[2]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def make_box(width, height, *, fill):
    return fill * (width * height)

# 함수 호출 후 width, height, fill 키워드 인자 넘기기
# 이후 반환값 출력
print(make_box(width, height, fill=fill))