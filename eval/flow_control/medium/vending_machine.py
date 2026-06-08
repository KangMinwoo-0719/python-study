money = int(input())
water = 500
juice = 1000
coffee = 1500

# 잔액이 부족해질때까지 반복:
while True:

    # 메뉴 선택 시 출력할 문구 저장
    menu_msg = ""

    # 현재 잔액이 물보다 적으면 종료
    if money < water:
        break

    # 현재 잔액 출력
    print(f"잔액: {money}원")

    # 메뉴 출력 후 정수로 메뉴 입력받기
    print(f"1. 물 ({water}원)")
    print(f"2. 주스 ({juice}원)")
    print(f"3. 커피 ({coffee}원)")
    menu = int(input())

    # 메뉴 입력 예외처리
    if menu < 0 or menu > 3:
        print("잘못된 선택입니다.")
        continue

    # 1번 입력 -> 500원 차감
    elif menu == 1:
        if money < water:
            print("잔액이 부족합니다.")
            break
        else:
            money -= 500
            menu_msg = "물"

    # 2번 입력 -> 1000원 차감
    elif menu == 2:

        # 잔액이 모자란 경우 break
        if money < juice:
            print("잔액이 부족합니다.")
            break
        else:
            money -= 1000
            menu_msg = "주스"

    # 3번 입력 -> 1500원 차감
    else:
        # 잔액이 모자란 경우 break
        if money < coffee:
            print("잔액이 부족합니다.")
            break
        else:
            money -= 1500
            menu_msg = "커피"

    # 각 메뉴별 저장된 메뉴선택문구 출력
    print(f"{menu_msg}를 선택했습니다.")

# 남은 금액 출력
print(f"남은 금액: {money}원")