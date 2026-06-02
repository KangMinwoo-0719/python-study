balance = int(input())
n = int(input())
lack_balance = False

# n값 만큼 반복:
for _ in range(n):

    # 명령어와 금액 공백을 기준으로 나누어 입력받기
    command, money = input().split()

    # DEPOSIT(입금) 명령어가 들어오면 금액 누적
    if command == "DEPOSIT":
        balance += int(money)

    # WITHDRAW(출금) 명령어인 경우:
    elif command == "WITHDRAW":

        # 현재 잔액이 부족하면 잔액 부족 출력
        if balance < int(money):
            lack_balance = True
            print("잔액 부족")

        # 많다면 현재 금액 - 출력 금액
        else:
            balance -= int(money)

    # 예외 처리
    else:
        print("DEPOSIT / WITHDRAW 중에서 입력해주세요.")

    # 각 분기 통과 후 현재 잔고 출력
    if not lack_balance:
        print(balance)

    # 깃발 초기화
    lack_balance = False