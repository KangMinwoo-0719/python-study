words = input().split()
words_dict = {}

# 단어 리스트를 순회하며 딕셔너리에 단어 추가
for word in words:
    words_dict[word] = words_dict.get(word, 0) + 1

# 생성된 딕셔너리 순회:
for word, count in words_dict.items():

    # 단어: 개수 형식으로 출력
    print(f"{word}: {count}")