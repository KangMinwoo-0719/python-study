students = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# value값이 cutoff보다 큰 사람들만 딕셔너리에서 순회하며 출력
accept_students = {
    name : score for name, score in students.items() if score >= cutoff
}

# 딕셔너리 순회하며 순차 출력
for name, score in accept_students.items():
    print(f"{name}: {score}")