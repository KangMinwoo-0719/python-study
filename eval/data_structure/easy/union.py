s1_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"A", "B"},
    {"X", "Y"},
]
s2_sets = [
    {"지우", "도윤", "예준", "하준"},
    {"A", "B", "C"},
    set(),
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 각 그룹의 합집합 구한 후 정렬 언패킹 출력
print(*sorted(s1.union(s2)))