text = input()

# 입력받은 문자열 처음과 마지막 문자를 제외하고 마스킹
result = text[0] + ("*" * len(text[0:-2])) + text[-1]

# 마스킹 결과 출력
print(f"마스킹 결과: {result}")