# 오른쪽을 가리키는 화살표 모양의 별 패턴을 출력하세요.
n = int(input())


# 1 ~ n + 1 범위만큼 반복:
for up_line in range(1, n + 1):

    # join을 통해 문자열 '*' 사이 공백 집어넣으며 출력
    print(" ".join('*' * up_line))

# n - 1 ~ 0 범위만큼 반복:
for down_line in range(n - 1, 0, -1):

# join을 통해 문자열 '*' 사이 공백 집어넣으며 줄여가며 출력
    print(" ".join('*' * down_line))