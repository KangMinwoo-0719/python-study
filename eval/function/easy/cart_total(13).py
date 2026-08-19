raw = input().split()
pos = [t for t in raw if "=" not in t]
items = [int(x) for x in pos]
coupon = 0
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "coupon":
            coupon = int(v)

def cart(*items, coupon=0):
    return sum(items) - coupon

# ↓ 호출부 (수정하지 마세요) — coupon 은 키워드 전용이라 이름으로 전달
print(cart(*items, coupon=coupon))