s1_sets = [
    {"윤서": 85, "지우": 92, "민준": 65},
    {"A": 70, "B": 80},
    {"X": 70},
]
s2_sets = [
    {"지우": 88, "민준": 70, "도윤": 95},
    {"A": 90, "B": 80},
    {"X": 70},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]
total = 0
# s1 set + s2 set의 평균 구한 후 출력
print(f"전체 평균: {(sum(s1.values()) + sum(s2.values())) / (len(s1) + len(s2)):.1f}")

# s1과 s2의 key값 set을 구한 후 해당 key의 value 평균 구하여 출력
s1_s2_set = set(s1.keys()) & set(s2.keys())
for name in s1_s2_set:
    total += s2[name]
avg = total / len(s1_s2_set)
print(f"양학기 2학기 평균: {avg:.1f}")