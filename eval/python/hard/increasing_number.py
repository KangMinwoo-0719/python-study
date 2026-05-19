# 10부터 N 사이의 증가수를 출력하세요.
N = int(input())

# 10 미만 예외처리
if N < 10:
    print("10 이상의 숫자를 입력해주세요")

# 10 ~ N + 1 범위 순회:
else:
    for num in range(10, N + 1):

        # 현재 숫자 문자열로 변환
        num = str(num)

        # 문자열 마지막 자리가 첫 번째 자리보다 크면 출력
        if num[-1] > num[0]:
            print(num)