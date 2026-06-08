s1_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"A", "B", "C"},
    {"X", "Y"},
]
s2_sets = [
    {"지우", "도윤", "예준", "하준"},
    {"A", "B"},
    {"P", "Q"},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 각 집합의 교집합을 정렬 후 언패킹 출력
print(*sorted(s1.intersection(s2)))