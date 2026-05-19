# 위쪽 삼각형과 아래쪽 역삼각형을 각각 for문으로 출력하세요.
n = int(input())


# n값만큼 라인 출력 반복(윗부분):
for line in range(1, n + 1):


    # n - line값 공백으로 출력 후 끌어오기
    print(" " * (n - line), end = "")

    # 2 * line - 1 만큼 출력
    print('*' * (2 * line - 1))


# n값 - 1만큼 라인 출력 반복(아랫부분):
for under_line in range(n - 1, 0, -1):

    # 라인 수 만큼 공백 출력 후 별 출력
    print(" " * (n - under_line) + "*" * (2 * under_line - 1))