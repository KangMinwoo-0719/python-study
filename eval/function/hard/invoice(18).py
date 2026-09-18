raw = input().split()
pos = [t for t in raw if "=" not in t]
base = int(pos[0])
items = [int(x) for x in pos[1:]]
tax = 0
fees = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "tax":
            tax = int(v)
        else:
            fees[k] = int(v)

# TODO: 여기에 함수 invoice(base, *items, tax=0, **fees) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def invoice(base, *items, tax=0, **fees):
    """
    기본가(base), 개수 품목(items), 세금(tax), 추가 비용(fees)을 입력받아
    base + (items 합) + base * tax // 100 + (fees 값들의 합) 값을 반환하는 함수
    """
    
    return base + sum(items) + base * tax // 100 + sum(fees.values())

# ↓ 호출부 (수정하지 마세요)
print(invoice(base, *items, tax=tax, **fees))