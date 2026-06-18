n = int(input())
reciept = {}
menu_count = []
index = 0
# n값 범위 반복:
for _ in range(n):

    # 종류, 개수, 가격을 "," 기준으로 나누어 입력받기
    menu, count, price = input().split(",")

    # 종류: 금액 x 개수 형태로 딕셔너리 빌딩
    reciept[menu] = int(price) * int(count)

    # 각 메뉴 개수 저장
    menu_count.append(count)

# 딕셔너리 순회:
for menu, price in reciept.items():

    # 입력받은 순서대로 종류 x 개수 : 금액 형식 출력
    print(f"{menu} x{menu_count[index]}: {price}원")

    # 메뉴 개수 카운트 리스트의 인덱스 증가
    index += 1

# 총 금액 출력
print(f"총액: {sum(reciept.values())}원")