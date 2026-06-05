text = input()
result = ''

# 입력받은 문자를 인덱스 번호와 함께 순회:
for index, char in enumerate(text):

    # 앞의 문자가 공백인 경우 또는 첫 번째면 현재 문자 upper
    if text[index - 1] == " " or index == 0:
        result += char.upper()
    else:
        result += char

# 결과 출력
print(result)