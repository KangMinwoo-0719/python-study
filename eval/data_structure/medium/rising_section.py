values = [int(x) for x in input().split()]


# 생성된 리스트 순회하며 현재 인덱스가 이전 인덱스보다 크면 갱신하여 누적
result = [idx for idx, value in enumerate(values) if values[idx] > values[idx - 1]]

# 상승이 없는 경우 상승 없음 출력
if not result or (len(result) == 1 and 0 in result):
    print("상승 없음")

# 상승이 있는 경우 언패킹 출력
else:
    print(*result)