cipher = input()
key = input()
replacement = ''

# 암호문 문자열 순회:
for char in cipher:

    # 공백의 경우 그대로 치환값에 삽입
    if char == " ":
        replacement += " "
        continue

    # 치환 키 인덱스 번호와 함께 순회:
    for index, key_char in enumerate(key):

        # 치환 키 현재 문자열이 암호문의 현재 문자열과 같은 경우:
        if key_char == char:

            # 치환값 -> 치환 키 현재 인덱스 - 1
            replacement += key[index - 1]
            break

# 치환값 출력
print(replacement)