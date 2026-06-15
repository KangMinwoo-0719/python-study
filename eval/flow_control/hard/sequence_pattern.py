n = int(input())
triangle_num = 0
total = 0

# 1 ~ n + 1 범위 반복:
for num in range(1, n + 1):

    # 삼각수에 현재 값 누적
    triangle_num += num

    # 현재 삼각수 출력
    print(f"T({num}) = {triangle_num}")

    # 전체값 누적
    total += triangle_num

# 합계 출력
print(f"합계: {total}")