words = input().split()
words_count = {}

# 리스트 순회:
for word in words:

    # 단어: 카운트 형식으로 딕셔너리 구성
    words_count[word] = words_count.get(word, 0) + 1

# 딕셔너리를 카운트, 단어 형식으로 튜플 패킹 후 내림차순 정렬
words_sorted = sorted([(-count, word) for word, count in words_count.items()])

# 리스트 순회:
for count, word in words_sorted:
    star = "*" * abs(count)
    # 단어: 카운트 x "*" 형식 출력
    print(f"{word}: {star}")