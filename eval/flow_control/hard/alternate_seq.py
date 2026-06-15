N = int(input())
total = 0

# 1 ~ N + 1 범위 반복:
for num in range(1, N + 1):

    # 현재 교대 수 구하기
    shift = 1 / num

    # 홀수 항이면 더하기
    if num % 2 != 0:
        total += shift
        print(f"{num}항까지의 합: {total:.4f}")

    # 짝수 항이면 빼기
    else:
        total -= shift
        print(f"{num}항까지의 합: {total:.4f}")