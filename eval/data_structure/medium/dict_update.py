main_sets = [
    {"수학": 80, "영어": 75, "과학": 90},
    {"A": 1, "B": 2},
    {"X": 10, "Y": 20},
]
update_sets = [
    {"영어": 88, "역사": 70},
    {"C": 3, "D": 4},
    {},
]
t = int(input())
main = main_sets[t]
update_data = update_sets[t]

# 두 딕셔너리를 병합하기
merged_data = main.copy() 
merged_data.update(update_data)

# 병합한 딕셔너리 순회:
for subject, score in merged_data.items():

    # 과목: 점수 형식으로 출력
    print(f"{subject}: {score}")