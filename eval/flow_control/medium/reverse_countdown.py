start = int(input())
step = int(input())

# start ~ 1 까지의 범위를 step으로 반복:
for num in range(start, 0, -step):

    # 숫자 출력 후 끌어오기
    print(num, end = " ")

# 종료 후 발사 출력
print()
print("발사!")