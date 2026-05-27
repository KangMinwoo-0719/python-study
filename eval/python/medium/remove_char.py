text = input()
remove = input()
result = ""

# 현재 텍스트 순회:
for char in text:

    # 문자열이 remove와 다른 경우 result에 저장
    if char != remove:
        result += char

# 결과 출력
print(f"결과: {result}")