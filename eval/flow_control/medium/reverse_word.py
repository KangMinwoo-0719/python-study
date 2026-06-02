text = input()
result = ""

# 입력받은 문자열 길이만큼 돌며 역순 저장
result = [text[index] for index in range(len(text) - 1, -1, -1)]

# 공백 제거하여 출력
print(f"뒤집은 문자열: {''.join(result)}")