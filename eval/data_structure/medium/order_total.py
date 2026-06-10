menu = {"커피": 4000, "라떼": 5000, "차": 3000, "케이크": 6000}
total = 0
n = int(input())

# n값만큼 메뉴 입력받은 후 리스트 생성
orders = [input() for order in range(n)]

# 주문 리스트 순회:
for order in orders:

    # 메뉴 딕셔너리에 해당 메뉴(key)와 가격 출력
    if order in menu.keys():
        print(f"{order}: {menu[order]}원")
        total += menu[order]

# 누적 값 출력
print(f"합계: {total}원")