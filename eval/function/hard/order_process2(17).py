raw = input().split()
pos = [t for t in raw if "=" not in t]
product = pos[0]
price = int(pos[1])
options = pos[2:]
discount = 0
info = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "discount":
            discount = int(v)
        else:
            info[k] = v

def order2(product, price, *options, discount=0, **info):
    """
    상품명(product), 가격(price - discount), 옵션(options), 할인율(discount), 기타 정보(info)
    를 입력 받아 "{product} {price}원 옵션{len(options)}개 [val=key]" 형식의 문자열을
    반환하는 함수
    """

    # 기타 정보의 key와 value를 "key=value" 형식으로 바꾸어 정렬 후 리스트로 저장하기
    info_unpack = sorted([f"{key}={val}" for key, val in info.items()])

    # 상품명, 가격 - 할인율, 옵션 개수와 기타 정보를 반환하기
    return f"{product} {price - discount}원 옵션{len(options)}개 [{','.join(info_unpack)}]"

# ↓ 호출부 (수정하지 마세요)
print(order2(product, price, *options, discount=discount, **info))