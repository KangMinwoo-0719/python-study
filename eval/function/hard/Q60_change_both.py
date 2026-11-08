def change_both(num, items):
    """
    정수 num과 정수 리스트 items를 받아
    num 정수에 100을 더하고 items 리스트에 0을 추가하는 함수
    """

    # num + 100, items 리스트에 0 추가하기
    num = num + 100
    items.append(0)

# 첫 값=정수 n, 나머지=리스트 items. 예: "5 1 2" → n=5, items=[1, 2]
parts = input().split()
num = int(parts[0])
items = [int(x) for x in parts[1:]]

# 함수 호출 후 num, items 리스트 인자값으로 넘겨주기
change_both(num, items)

# num과 items 출력하기
print(num)
print(items)