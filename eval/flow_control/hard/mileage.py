# while True, if/elif로 구현하세요.
mileage = 0
total_earned = 0
total_used = 0
rate = 5


# 프로그램 종료 전 까지 반복:
while True:

    # 마일리지 시스템 메뉴 출력
    print("===== 마일리지 시스템 =====")
    print("1. 구매 (마일리지 적립)")
    print("2. 마일리지 사용")
    print("3. 마일리지 조회")
    print("4. 종료")

    # 메뉴 정수로 입력받기
    menu = int(input())

    # 1을 입력받은 경우 금액 입력받기
    if menu == 1:
        price = int(input())

        # 0 이하면 양수 입력하라는 문구 출력
        if price <= 0:
            print("구매 금액은 양수여야 합니다.")

        # 정상 입력 시 마일리지 계산 후 마일리지 적립금 출력
        else:
            earned = (price * rate) // 100
            mileage += earned
            total_earned += earned
            print(f"{mileage} 마일리지가 적립되었습니다!")

    # 2를 입력받은 경우 마일리지 조회:
    elif menu == 2:

        # 마일리지가 0 이하면 없다고 출력
        if mileage <= 0:
            print("보유 마일리지가 없습니다.")

        # 있으면 사용값 입력받기:
        else:
            used_earned = int(input())

            # 입력값 0 이하면 1 이상의 값 출력하라는 문구 출력
            if used_earned <= 0:
                print("1 이상의 값을 입력해 주세요.")
            
            # 보유한 마일리지 값 보다 크면 마일리지 부족 문구와 보유 마일리지 출력
            elif used_earned > mileage:
                print(f"마일리지가 부족합니다. (보유: {mileage})")

            # 정상 입력 시 마일리지 사용, 사용 후 남은 마일리지 출력
            else:
                mileage -= used_earned
                total_used += used_earned
                print(f"{used_earned} 마일리지를 사용했습니다.")
                print(f"남은 마일리지: {mileage}")

    # 3을 입력받은 경우 마일리지 조회, 사용한 마일리지 출력
    elif menu == 3:
        print(f"보유 마일리지: {mileage}")
        print(f"총 적립: {total_earned} / 총 사용: {total_used}")

    # 4를 입력받으면 종료 문구 출력 후 break
    elif menu == 4:
        print("이용해 주셔서 감사합니다.")
        break

    # 그 외의 잘못된 입력 처리
    else:
        print("잘못된 메뉴입니다.")

    print()