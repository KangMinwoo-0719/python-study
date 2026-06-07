words = input().split()

# 해당 단어와 매칭하는 인덱스 value 리스트에 생성
words_dict = {word: [index for index, char in enumerate(words) if char == word] for index, word in enumerate(words)}

# 딕셔너리 정렬 순회:
for word, index in sorted(words_dict.items()):

    # key: value 형식으로 출력
    print(word + ":", *index)