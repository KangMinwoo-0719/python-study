# print(값, end="\t")로 탭 구분 출력을 만드세요.
n = int(input())

# 헤더의 X 출력
print('X', end = "\t")

# 입력받은 n값 만큼 반복:
for header in range(1, n + 1):

    # 헤더의 맨 위 숫자 순차적 출력
    print(header, end = "\t")


print()
print("-" * 30)

# 뒷 라인 곱셈 숫자 라인 구분:
for line in range(1, n + 1):

    # 맨 앞자리 숫자 출력
    print(line, end = "\t")

    # 한 라인의 숫자 출력을 위한 반복:
    for num in range(1, n + 1):

        # 곱셈 결과값 출력
        print(num * line, end = "\t")

    print()