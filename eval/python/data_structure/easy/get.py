scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 입력값 value 출력, 만약 없으면 0 출력
print(scores.get(name, 0))