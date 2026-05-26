a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

answer = 0

# a, b 리스트 동시에 순회:
for val_a, val_b in zip(a, b):

    # 각 인덱스 위치의 값이 같으면 누적
    if val_a == val_b:
        answer += 1

# 맞춘 값 / 요소 개수 계산 후 저장
correct = answer / len(a) * 100

# 일치율 소수점 한 자리로 맞춰 출력
print(f"일치율: {correct:.1f}%")