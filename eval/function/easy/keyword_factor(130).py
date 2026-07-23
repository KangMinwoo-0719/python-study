opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

def rectangle_kw(width, height):
    """
    opts 딕셔너리의 키 값(width, height)를 받아
    넓이를 계산하여 반환하는 함수

    reatangle_kw(4, 5) -> 20

    Args: width(int), height(int)
    Returns: int
    """
    return width * height

# opts 를 ** 로 풀어 키워드 인자로 전달
print(rectangle_kw(**opts))