opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

def total_with_tax(price, tax):
    """
    가격(price)과 세금(tax)를 받아
    price + price * tax // 100의 값을 반환하는 함수
    """

    # price + price * tax // 100의 값을 반환하기
    return price + price * tax // 100

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(total_with_tax(**opts))