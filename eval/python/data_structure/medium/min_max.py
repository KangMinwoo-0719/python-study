data = [10, 20, 30, 40, 50, 60, 70, 80]
n = int(input())

# data의 n - 1번째 인덱스까지의 min, max값 구하기
max_num = max(data[:n])
min_num = min(data[:n])

# 정규화 식을 저장하여 언패킹 출력
print(*[f"{(value - min_num) / (max_num - min_num):.2f}" for value in data[:n]])