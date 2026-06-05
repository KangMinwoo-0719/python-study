text = input()

# 텍스트를 인덱스 번호와 함께 순회하여 인덱스가 짝수면 대문자, 아닌 경우 소문자로 저장
result = [char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(text)]

# 결과 출력
print("".join(result))