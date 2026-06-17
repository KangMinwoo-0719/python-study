s1_sets = [
    {"윤서", "지우", "민준"},
    {"A", "B", "C"},
    {"X", "Y"},
]
s2_sets = [
    {"지우", "민준", "도윤", "예준"},
    {"A", "B", "C"},
    {"P", "Q"},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 1학기만 있는 학생(s1 - s2)
first_semester = sorted(s1 - s2)

# 2학기만 있는 학생(s2 - s1)
second_semester = sorted(s2 - s1)

# 양 학기에 있는 학생(교집합)
both_semester = sorted(s1 & s2)

print("1학기만:", *first_semester)
print("2학기만:", *second_semester)
print("양학기:", *both_semester)
