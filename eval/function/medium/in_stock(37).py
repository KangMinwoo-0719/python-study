def in_stock(num):
    """
    매개변수 num을 받아
    전역변수 stock보다 작은 경우(이하) "가능",
    초과인 경우 "불가"를 반환하는 함수
    """

    # num이 stock 이하이면 "가능", 초과인 경우 "불가" 반환
    return "가능" if num <= stock else "불가"

parts = input().split()
num = int(parts[0])
stock = int(parts[1])

# 함수 호출 후 반환값 출력
print(in_stock(num))