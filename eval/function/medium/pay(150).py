raw = input().split()
pos = [t for t in raw if "=" not in t]
price = int(pos[0])
fees = [int(x) for x in pos[1:]]
discount = 0
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "discount":
            discount = int(v)

# TODO: 여기에 함수 pay(price, *fees, discount=0) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def pay(price, *fees, discount=0):
    """
    가격(price), 추가 요금(fees), 할인액(discount)을 받아
    price + fees - discount 값을 반환하는 함수
    """

    return price + sum(fees) - discount

# ↓ 호출부 (수정하지 마세요) — discount 는 키워드 전용이라 이름으로 전달
print(pay(price, *fees, discount=discount))