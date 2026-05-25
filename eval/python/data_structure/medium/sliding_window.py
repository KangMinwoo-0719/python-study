data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = int(input())
w = int(input())

# i ~ i + w 인덱스 슬라이싱 출력
print(*data[i:i + w])