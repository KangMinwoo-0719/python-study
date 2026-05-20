n = int(input())
flag = False

# 단어들을 리스트로 받기
words = [input() for _ in range(n)]

# 마지막 단어와 첫 단어 각각 할당
for index in range(1, n):

    # 마지막 단어와 현재 단어의 각 끝과 처음 문자열이 다르면
    # 끊김 출력
    last_word = words[index - 1]
    current_word = words[index]

    if last_word[-1] != current_word[0]:
        print(f"끊김: {index + 1}번째 단어 '{current_word}'")
        break

# 아닌 경우 성공
else:
    print("성공")