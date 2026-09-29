# 거래 종류를 판별하여 잔액을 관리하세요.
balance = int(input())

# 3번 반복:
for _ in range(3):

    # 명령어, 금액 또는 명령어만 입력받기
    command = input().split()

    # 조회인 경우 현재 금액 출력
    if "조회" in command:
        print(f"현재 잔액: {balance}원")

    # 입금일 경우 입력받은 금액 누적
    elif "입금" in command:
        balance += int(command[1])
        print(f"입금 완료: 잔액 {balance}원")

    # 출금일 경우 현재 잔액 확인
    elif "출금" in command:

        # 잔액 부족인 경우 출금 실패
        if balance < int(command[1]):
            print("출금 실패: 잔액 부족")
            continue

        # 정상인 경우 출금 후 남은 잔액 출력
        balance -= int(command[1])
        print(f"출금 완료: 잔액 {balance}원")

# 최종 잔액 출력
print(f"최종 잔액: {balance}원")