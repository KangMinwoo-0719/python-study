# 빈 다이아몬드를 출력하세요.
n = int(input())


# 입력받은 1 ~ n값 // 2 + 2 만큼 up line 반복:
for up_line in range(1, n // 2 + 2):

    # line 값이 1인 경우 공백 * up line + 별 출력
    if up_line == 1:
        print(' ' * (n // 2) + '*')

    # 아닌 경우
    else:

        # 공백 * ((n // 2 + 1)- up_line) + 별 + 공백 * (up line - 1)*2-1 + 별 출력
        print(' ' * ((n // 2 + 1) - up_line)  + '*' + ' ' * ((up_line - 1) * 2 - 1) + '*')


# n // 2 + 1 ~ 1 범위만큼 down line 반복:
for down_line in range(n // 2 + 1, 1, -1):

    # down line의 값이 1이 되면 공백 * n // 2 + 별 출력
    if down_line == 2:
        print(' ' * (n // 2) + '*')

    # 아닌 경우:
    else:
    
        # 공백 * (n // 2 + 2 - down) + 별 + 공백 * ((down - 2) * 2 - 1) + 별 출력
        print(' ' * ((n // 2 + 2) - down_line) + '*' + ' ' * ((down_line - 2) * 2 - 1) + '*')