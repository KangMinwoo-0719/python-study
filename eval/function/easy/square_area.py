def area(w, h):
    """
    가로(w)와 세로(h)를 정수로 입력받으면 곱하여
    직사각형의 넓이를 반환하는 함수
    """

    return w * h


w, h = [int(x) for x in input().split()]

# 함수를 호출하여 반환값을 출력
print(area(w, h))