n = int(input())
words = set([])

# n값만큼 반복:
for _ in range(n):

    # 단어 입력받기
    word = input()

    # 입력받은 단어 add하기
    words.add(word)


# 결과값 정렬 출력
print(*sorted(words))