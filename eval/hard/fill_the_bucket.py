# 물통에 물을 순서대로 부어 넘치는 시점을 찾으세요.
c, n = map(int, input().split())
total = 0

# 물 개수만큼 반복:
for num in range(1, n + 1):

    # 넣을 물 정수로 입력받기
    water = int(input())

    # 누적하기
    total += water

    # 누적 값 > 용량이 될 경우 몇 번째에서 넘쳤는지 출력
    # 전체 누적 용량 - 용량 값 출력 후 break
    if total > c:
        print(f"{num}번째에서 넘침! 넘친 양: {total - c}")
        break

# 넘치지 않은 경우 출력
if total < c:
    print("안 넘침")