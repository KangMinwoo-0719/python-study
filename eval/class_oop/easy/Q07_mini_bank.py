class Account:
    """
    사용자 명과 초기 잔액을 입력받아
    이후 입력받는 금액을 입금하는 클래스
    """
    def __init__(self, owner, balance):
        """
        인스턴스 속성을 저장하는 메서드
        """

        # 인스턴스 속성 정의하기
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        초기 잔액 + 입력 금액의 값을 누적하는 함수
        """
        # 입력받은 금액(amount)을 초기 잔액(balance)에 누적하기
        self.balance += amount

    def get_balance(self):
        """
        누적된 현재 금액의 값을 반환하는 함수
        """
        # 현재 누적되어 있는 계좌 값 반환하기
        return self.balance

# 첫 줄: "예금주 초기잔액" (예: "kim 1000" -> owner="kim", balance=1000)
# 둘째 줄: 입금액들 (예: "500 300" -> [500, 300])
owner, balance = input().split()
balance = int(balance)
deposits = [int(x) for x in input().split()]


# ---- 호출부 (수정 금지) ----
acc = Account(owner, balance)
print(f"{acc.owner} 초기 잔액 {acc.get_balance()}")
for amount in deposits:
    acc.deposit(amount)
    print(f"입금 {amount} -> 잔액 {acc.get_balance()}")