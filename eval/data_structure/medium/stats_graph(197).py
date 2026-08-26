parts = input().split()
scores = []
rank_a = ''
rank_b = ''
rank_c = ''
rank_d = ''
rank_f = ''

# 점수 리스트 순회:
for part in parts:

    # 90 이상인 경우 A 등급 별 + 1
    if int(part) >= 90:
        rank_a += '*'

    # 80 이상 90 미만인 경우 B 등급 별 + 1
    elif int(part) >= 80:
        rank_b += '*'

    # 70 이상 80 미만인 경우 C 등급 별 + 1
    elif int(part) >= 70:
        rank_c += '*'

    # 60 이상 70 미만인 경우 D 등급 별 + 1
    elif int(part) >= 60:
        rank_d += '*'

    # 60 미만인 경우 F 등급 별 + 1
    else:
        rank_f += '*'

# 각 등급 카운터 별 출력]
print(f"A: {rank_a}")
print(f"B: {rank_b}")
print(f"C: {rank_c}")
print(f"D: {rank_d}")
print(f"F: {rank_f}")