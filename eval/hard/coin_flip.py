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

    # 연속(streak)이 최대 연속 정답(best_streak)보다 값이 크면 값 갱신
    if streak > best_streak:
        best_streak = streak


    # 앞면(1)을 입력받으면 아래 조건 확인:
    if num == 1:

        # round_num이 홀수면 정답 -> 연속(streak), 정답 + 1 후 출력
        if round_num % 2 == 1 and round_num % 3 != 0:
            streak += 1
            total_correct += 1
            print(f"동전: 앞! 정답! (연속 {streak}회)")

        # round_num이 홀수이지만 3의 배수면 오답
        elif round_num % 2 == 1 and round_num % 3 == 0:
            streak = 0
            print(f"동전: 앞! 틀렸습니다! (연속 기록 초기화)")

        # round num이 짝수이지만 3의 배수면 정답
        elif round_num % 2 == 0 and round_num % 3 == 0:
            streak += 1
            total_correct += 1
            print(f"동전: 앞! 정답! (연속 {streak}회)")

        # 그냥 짝수면 정답
        else:
            streak = 0
            print(f"동전: 앞! 틀렸습니다! (연속 기록 초기화)")


    # 뒷면(2)을 입력받으면 아래 조건 확인:
    elif num == 2:

        # round_num이 짝수면 정답 -> 연속(streak), 정답 + 1 후 출력
        if round_num % 2 == 0 and round_num % 3 != 0:
            streak += 1
            total_correct += 1
            print(f"동전: 뒤! 정답! (연속 {streak}회)")

        # round_num이 짝수지만 3의 배수인 경우 오답
        elif round_num % 2 == 0 and round_num % 3 == 0:
            streak = 0
            print(f"동전: 뒤! 틀렸습니다! (연속 기록 초기화)")

        # round num이 홀수지만 3의 배수면 정답
        elif round_num % 2 == 1 and round_num % 3 == 0:
            streak += 1
            total_correct += 1
            print(f"동전: 뒤! 정답! (연속 {streak}회)")

        # 그냥 홀수면 오답
        else:
            streak = 0
            print(f"동전: 뒤! 틀렸습니다! (연속 기록 초기화)")

    
    # 종료(0)을 입력받으면 반복 종료
    elif num == 0:
        break

    # 예외 처리
    else:
        print("잘못된 입력입니다. 1 / 2 / 0 중에 선택해주세요.")

    # 한 게임이 끝나면 total game, round num + 1 누적
    total_games += 1
    round_num += 1

# 게임 결과 메시지 출력
print()
print("=== 게임 결과 ===")
print(f"총 게임: {total_games}회")
print(f"정답: {total_correct}회")
print(f"최대 연속 정답: {best_streak}회")