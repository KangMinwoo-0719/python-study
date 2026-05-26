# 숫자 다이아몬드를 출력하세요.
n = int(input())


# 입력받은 정수 1 ~ n // 2 + 2 범위만큼 up line 반복:
for up_line in range(1, n // 2 + 2):

    # 앞에 올 공백값 먼저 출력 후 숫자 끌어오기
    print(' ' * ((n // 2 + 1) - up_line), end = "")

    # 라인 안에서 오름차순 숫자 1 ~ up_line 범위만큼 반복:
    for up_num in range(1, up_line + 1):

        # up_num 출력 후 끌어오기
        print(up_num, end = "")

    # 라인 안에서 내림차순 출력할 숫자만큼 반복:
    for down_num in range(up_line - 1, 0, -1):

        # down_num 출력 후 끌어오기
        print(down_num, end = "")

    # 줄바꿈
    print()

# n // 2 ~ 0 범위만큼 down line 반복:
for down_line in range(n // 2, 0, -1):

    # 앞에 올 공백값 먼저 출력 후 숫자 끌어오기
    print(' ' * ((n // 2 + 1) - down_line), end = "")

    # 라인 안에서 오름차순 숫자 1 ~ down line + 1 범위만큼 반복
    for up_num2 in range(1, down_line + 1):

        # up_num2 출력 후 끌어오기
        print(up_num2, end = "")

    # 라인 안에서 내림차순 출력할 숫자만큼 반복:
    for down_num2 in range(down_line - 1, 0, -1):

        # down_num2 출력 후 끌어오기
        print(down_num2, end = "")

    # 줄바꿈
    print()