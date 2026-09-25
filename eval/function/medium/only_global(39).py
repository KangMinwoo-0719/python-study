def tax_of():
    global amount
    global rate

    # print(amount)
    
    return amount * rate // 100

# 전역 amount = 첫 값, rate = 둘째 값. 예: "1000 10" → amount=1000, rate=10
parts = input().split()
amount = int(parts[0])
rate = int(parts[1])

# 함수 호출 후 반환값 출력
print(tax_of())