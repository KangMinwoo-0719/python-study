num = int(input())
total = 0

# num이 0이 되기 전 까지 반복:
while num > 0:

    # num 뒷자리 하나씩 분리
    digit = num % 10

    # 새로운 변수에 값 누적
    total += digit

    # num에서 뒷자리 하나씩 제거
    num //= 10

# 각 자릿수 합 출력
print(f"각 자릿수의 합: {total}")