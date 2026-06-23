tables = [
    [[10, 20, 30, 40],
     [5, 15, 25, 35],
     [0, 10, 20, 30]],
    [[7, 7, 7],
     [1, 2, 3]],
    [[100, 50]],
    [[2, 10, 3, 1],
     [4, 20, 1, 2]],
    [[1, 1, 1, 1, 1],
     [2, 2, 9, 2, 2],
     [1, 1, 1, 1, 1]],
    [[3],
     [4],
     [5]],
    [[9, 1, 2],
     [8, 0, 1]],
]
t = int(input())          # 시나리오 번호 (0~4)
table = tables[t]         # tables 에서 t 번째 2차원 표 선택
max_total = 0
max_quarter = []

# 현재 테이블의 열을 인덱스 번호로 순회:
for index in range(len(table[0])):

    # 현재 열의 n번째 요소 ~ 마지막 열 요소 리스트에 저장
    result = [col[index] for col in table]

    # 리스트 합 출력
    current = sum(result)
    max_quarter.append(current)

    # 현재 요소의 합이 이전 값보다 크면 최고 분기 인덱스 갱신
    if current > max_total:
        max_total = current
        max_index = index

# 최고 분기 출력
print(*max_quarter)
print(f"최고 분기: {max_index}")