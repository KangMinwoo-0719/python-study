raw = input().split()
pos = [t for t in raw if "=" not in t]
product = pos[0]
price = int(pos[1])
options = pos[2:]
discount = 0
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "discount":
            discount = int(v)

def order(product, price, *options, discount=0):
    """
    상품명(product), 가격(price), 임의 옵션(options), 할인(discount)을 받아
    "{product} {price - discount}원 옵션{len(options)}개" 형식의 
    문자열을 반환하는 함수
    """

    # 상품명, 가격, 옵션 수를 반환
    return f"{product} {price - discount}원 옵션{len(options)}개"

# ↓ 호출부 (수정하지 마세요) — discount 는 키워드 전용이라 이름으로 전달
print(order(product, price, *options, discount=discount))