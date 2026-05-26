# if/elif로 모드 분기 후 while로 변경 과정 출력
current_temp = int(input())
target_temp = int(input())


# 현재 온도가 목표 온도보다 낮으면 난방모드:
if current_temp < target_temp:
    print("난방 모드를 시작합니다.")

    # 현재 온도를 반복하면서 출력
    while current_temp < target_temp:
        print(f"현재 온도: {current_temp}도 → {current_temp + 1}도")
        current_temp += 1

    # 목표 온도 출력
    print(f"목표 온도 {target_temp}도에 도달했습니다!")


# 현재 온도가 목표 온도보다 높으면 냉방모드:
elif current_temp > target_temp:
    print("냉방 모드를 시작합니다.")

    # 현재 온도 반복하면서 출력
    while current_temp > target_temp:
        print(f"현재 온도: {current_temp}도 → {current_temp - 1}도")
        current_temp -= 1

    # 목표 온도 출력
    print(f"목표 온도 {target_temp}도에 도달했습니다!")


# 똑같으면 예외 처리
else:
    print("이미 목표 온도입니다.")