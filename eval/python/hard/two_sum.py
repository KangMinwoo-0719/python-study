# 합이 target인 두 수의 쌍을 출력하세요.
N = int(input())
target = int(input())

# 1 ~ N + 1값 반복:
for first in range(1, N + 1):

    # target - a값 지정
    second = target - first

    # first보다 크고 입력값보다 작으면(이하) 출력
    if first < second <= N:
        print(f"({first}, {second})")