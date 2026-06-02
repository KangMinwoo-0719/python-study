scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 입력받은 값의 key로 이동하여 delete
del scores[name]
for key in scores:
    print(f"{key}: {scores[key]}")