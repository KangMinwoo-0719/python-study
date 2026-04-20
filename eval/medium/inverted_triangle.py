# range(n, 0, -1)은 n부터 1까지 감소합니다.
n = int(input())


# 입력받은 n ~ 0까지의 값 만큼 줄 반복:
for star in range(n, 0, -1):

    # "*" * star 값 출력 후 끌어오기
    print("*" * star)