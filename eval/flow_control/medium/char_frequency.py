text = input()
count = 0

# 문자열 순회:
for char in text:

    # 현재 문자열을 기준으로 텍스트 순회:
    for find_char in text:

        # 같은 텍스트 카운트
        if find_char == char:
            count += 1

    # 현재 문자열: 개수 형식으로 출력
    print(f"{char}: {count}개")
    count = 0