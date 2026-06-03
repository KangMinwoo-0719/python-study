scores = [85, 92, 65, 78, 95, 70, 88, 72, 90, 100]
cutoff = int(input())

# scores 리스트에서 cutoff 이하인 정수만 카운트
accepted = [1 for score in scores if score <= cutoff]

# 카운트 / 전체 길이 * 100 -> 백분위 출력
avg = sum(accepted) / len(scores) * 100
print(f"백분위: {avg:.1f}")