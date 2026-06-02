# 모래시계 패턴을 출력하세요.
n = int(input())


# 1 ~ n // 2 + 2 범위만큼 라인 반복:
for up_line in range(1, n // 2 + 2):

    # 윗 라인 공백 출력 후 별 붙여 출력
    print(" " * (up_line - 1) + "*" * (n - (up_line * 2 - 1) + 1))

# 2 ~ n // 2 + 1 까지의 범위만큼 라인 반복:
for down_line in range(2, n // 2 + 1):

    # ' ' * (up_line - down_line) + '*' * (2 * down_line - 1) 값 출력하기
    print(' ' * (up_line - down_line) + '*' * (down_line * 2 - 1))