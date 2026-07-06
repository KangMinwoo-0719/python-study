def paint():
    """
    전역변수 color(str)의 값을 바꾼 후 반환하는 함수

    args : None
    return : str
    """
    color = inner
    return color

parts = input().split()
color = parts[0]
inner = parts[1]

# 함수 호출 후 반환값 출력
print(paint())

# 기본 입력값 출력
print(color)