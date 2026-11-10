class Product:
    """
    상품명과 원가를 받은 후
    차례대로 입력받은 할인율을 적용한 값을 계산하는 클래스
    """

    def __init__(self, name, price):
        """
        인스턴스 속성 name, price를 정의하는 생성자
        """
        self.name = name
        self.price = price

    def discounted(self, percent):
        """
        입력받은 할인율을 적용한 값을 반환하는 메서드
        """
        # 입력받은 할인율을 적용한 값을 반환
        return self.price * (100 - percent) // 100

# 첫 줄: "상품명 정가" (예: "노트북 1200000" -> name="노트북", price=1200000)
# 둘째 줄: 할인율(%)들 (예: "10 20" -> [10, 20])
name, price = input().split()
price = int(price)
percents = [int(x) for x in input().split()]

# ---- 호출부 (수정 금지) ----
p = Product(name, price)
for percent in percents:
    print(f"{p.name} {percent}% 할인가 {p.discounted(percent)}")
print(f"정가 {p.price}")