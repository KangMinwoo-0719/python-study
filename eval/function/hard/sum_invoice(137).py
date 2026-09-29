opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# TODO: 여기에 함수 invoice(base, **fees) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def invoice(base, **fees):
    """
    기본가(base), 추가 항목(fees)을 받아
    기본가 + 추가항목 가격 값을 반환하는 함수
    """
    return base + sum(fees.values())

# ↓ 호출부 (수정하지 마세요) — base 는 base 매개변수로, 나머지는 **fees 로 모임
print(invoice(**opts))