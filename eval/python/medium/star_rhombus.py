n = int(input())

# 상위 라인 반복:
for up_line in range(1, n // 2 + 2):

    # 순차적으로 삼각형 모양 출력
    print(' ' * ((n // 2 + 1) - up_line) + '*' * (up_line * 2 - 1))

# 하위 라인 반복:
for under_line in range(1, n // 2 + 1):

    # 역삼각형 모양으로 출력
    print(' ' * (under_line) + '*' * (n - 2))
    n -= 2