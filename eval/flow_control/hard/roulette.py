ANSWER = 7
max_chance = 3

# 룰렛 시작 문구 출력
print("=== 행운의 룰렛 ===")
print(f"1~10 중 숫자를 맞춰보세요! (기회: {max_chance}번)")
print()

# 기회가 0이 아닌 경우 계속 반복:
while max_chance != 0:

    # 정수 입력받기
    num = int(input())

    # 정답인 경우 맞췄다는 문구 출력과 함께 break
    if num == ANSWER:
        print("정답입니다! 축하합니다!")
        break

    # 맞추지 못한 경우 아래 조건 확인
    else:

        # chance - 1
        max_chance -= 1

        # 정답 - 입력값 또는 입력값 - 정답 == 1이면 매우 가깝다는 문구 출력
        if ANSWER - num == 1 or num - ANSWER == 1:
            print(f"아주 가까워요! (뜨거워!) (남은 기회: {max_chance}번)")

        # 2 ~ 3이면 가깝다는 문구 출력
        elif 2 <= ANSWER - num <= 3 or 2 <= num - ANSWER <= 3:
            print(f"가까워요! (따뜻해요) (남은 기회: {max_chance}번)")

        # 4 이상이면 멀다는 문구 출력
        else:
            print(f"멀어요... (차가워요) (남은 기회: {max_chance}번)")

        # 기회가 모두 없어지면(chance == 0) 정답 출력과 함께 break
        if max_chance == 0:
            print(f"기회를 모두 사용했습니다. 정답은 {ANSWER}이었습니다.")
            break