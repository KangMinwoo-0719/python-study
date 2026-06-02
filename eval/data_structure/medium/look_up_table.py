n = int(input())

# 딕셔너리를 생성 후 바로 key, value를 순회 후 출력
for num, square in {value : value * value for value in range(1, n + 1)}.items():
    print(f"{num}: {square}")