# i==0 또는 i==n-1 또는 j==0 또는 j==n-1 이면 테두리입니다.
n = int(input())


# 0 부터 입력받은 n 까지의 범위 반복하기:
for line in range(n):

    # line == 0 이거나 n - 1의 값과 같으면 테두리 -> 정상 출력
    if line == 0 or line == n - 1:
        print("*" * n)

    # 테두리가 아닌 경우 -> 입력받은 n - 2 만큼의 공백값 사이에 넣고 출력
    else:
        print('*' + " " * (n - 2) + "*")