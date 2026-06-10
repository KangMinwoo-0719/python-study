numbers = {1, 5, 3, 8, 2, 10, 7, 4}
cutoff = int(input())

# set에서 cutoff 이상인 정수만 필터링 후 오름차순 정렬
result = sorted([num for num in numbers if num >= cutoff])

# 공백을 사이에 넣고 출력
print(" ".join(map(str, result)))