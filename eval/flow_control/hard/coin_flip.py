round_num = 1
streak = 0
best_streak = 0
total_correct = 0
total_games = 0


# 게임 메뉴 출력
print("=== 동전 뒤집기 게임 ===")
print("앞(1) 또는 뒤(2)를 맞춰보세요! (종료: 0)")
print()

# 종료(0)를 입력받기 전 까지 반복:
while True:

    # 정수(1, 2, 0)중 하나 입력받기:
    num = int(input())
    
    # 종료(0)을 입력받으면 반복 종료
    if num == 0:
        break

    # 홀수 True값 저장
    coin_odd = round_num % 2 == 1

    # 3의 배수 True값 저장
    coin_triple = round_num % 3 == 0

    # 결과 반전값 포함하여 저장
    correct = 2 if(coin_odd == coin_triple) else 1

    # 동전 앞 뒤 정하기
    coin_face = "앞" if correct == 1 else "뒤"

    # 정답 결과와 맞으면 연속 정답, 총 정답 + 1
    if num == correct:
        streak += 1
        total_correct += 1
        print(f"동전: {coin_face}! 정답! (연속 {streak}회)")

    # 틀린 경우 연속 정답 초기화
    else:
        print(f"동전: {coin_face}! 틀렸습니다! (연속 기록 초기화)")
        streak = 0

    # 최고 기록이 현재 연속보다 작으면 새로 갱신
    if best_streak < streak:
            best_streak = streak

    # 총 게임, 라운드 + 1
    total_games += 1
    round_num += 1


# 게임 결과 메시지 출력
print()
print("=== 게임 결과 ===")
print(f"총 게임: {total_games}회")
print(f"정답: {total_correct}회")
print(f"최대 연속 정답: {best_streak}회")