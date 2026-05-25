grids = [
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
    [[1, 2, 3], [4, 5, 6]],
    [[1], [2], [3]],
]
t = int(input())
grid = grids[t]

# 현재 중첩 리스트의 행 -> 열 순서로 차례대로 저장
result = [col for row in grid for col in row]

# 결과값 출력
print(*result)