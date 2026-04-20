# print(j, end="")을 사용해 줄바꿈 없이 이어서 출력하세요.
n = int(input())


# 입력받은 n값 만큼 라인 반복:
for line in range(1, n + 1):

    # 한 라인에서 출력할 숫자 반복:
    for num in range(1, line + 1):

        # num 값 출력 후 끌어오기
        print(num, end = "")

    print()