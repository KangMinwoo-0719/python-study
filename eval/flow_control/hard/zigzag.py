n = int(input())
m = int(input())

# 각 라인에서 출력할 숫자를 지정할 변수
block = 1

# 입력받은 줄 수(1 ~ n + 1) 범위만큼 라인 반복:
for line in range(1, n + 1):

    # 라인이 짝수이면 숫자 앞 공백 출력
    if line % 2 == 0:
            print(' ' * (m * 2), end = "")

    # 라인에서 출력할 숫자 반복
    for num in range(block, (m * n + 1)):

        # 라인에서 숫자 출력
        print(f"{num} ", end = "")

        if num % m == 0:
            break

    print()

    # 다음 라인에서 출력할 숫자 지정
    block += m