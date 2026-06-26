weights = [int(x) for x in input().split()]
found = False
total = 0
count = 0

# 리스트 순회:
for weight in weights:

    # 무게가 0인 경우 건너뛰기
    if weight == 0:
        continue

    # 30kg을 초과하는 택배 발견 시 작업 중단
    elif weight > 30:
        found = True
        break

    # 그 외는 정상 작업
    else:
        total += weight
        count += 1

# 과적 발견 시 작업한 분량 무게와 개수 출력
if found:
    print(f"과적 발견: {weight}kg")
    print(f"처리한 택배: {count}개, 총 {total}kg")

# 정상 처리 시 작업한 분량 무게와 개수 출력
else:
    print(f"전량 처리 완료: {count}개, 총 {total}kg")