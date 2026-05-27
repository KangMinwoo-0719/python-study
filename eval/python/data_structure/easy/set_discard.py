fruits = {"apple", "banana", "cherry", "date", "fig"}
item = input()

# 집합에서 item 제거 후 언패킹 정렬 출력
fruits.discard(item)
print(*sorted(fruits))