data = [10, 20, 30, 40, 50]
n = int(input())

# 평균값 계산
mean = sum(data[:n]) // len(data[:n])

# list에서 각 요소들 - 평균값 n번째 인덱스까지 저장
result = [(val - mean) for val in data[:n]]

# 결과 출력
print(*result)