coords = [int(x) for x in input().split()]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def make_point(x, y):
    return "(" + str(x) + ", " + str(y) + ")"

# coords 를 * 로 풀어 make_point 에 넘기고, 그 반환값을 출력
print(make_point(*coords))