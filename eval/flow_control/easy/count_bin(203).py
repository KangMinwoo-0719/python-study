num = int(input())
one_count = 0

# 입력받은 숫자가 1 이상인 경우 계속 반복:
while num > 0:

    # 숫자를 2로 나누어 나머지가 1인 경우 카운트
    if num % 2 == 1:
        one_count += 1

    # 원본 숫자 갱신
    num = num // 2

# 총 1의 개수 출력
print(one_count)