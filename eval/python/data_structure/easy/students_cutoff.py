scores = [85, 92, 65, 78, 95]
cutoff = int(input())


# list에서 cutoff 이상인 value만 카운트하여 출력
result = [value for value in scores if value >= cutoff]
print(len(result))