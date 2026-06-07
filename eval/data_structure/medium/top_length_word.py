text = input().split()
top_word = ''

# 리스트 순회:
for word in text:

    # 현재 단어의 길이 저장
    word_len = len(word)

    # 현재 단어의 길이가 더 길면 갱신:
    if word_len > len(top_word):
        top_word = word

# 최대 길이 단어 출력
print(top_word)