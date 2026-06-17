n = int(input())
words_dict = {}

# n값 범위 반복:
for _ in range(n):

    # 단어:정의 형식 입력받은 후 딕셔너리 구성
    word, define = input().split(":")
    words_dict[word] = define


# 조회할 단어 입력받기
search_word = input()

# 단어가 있으면 정의, 없으면 없음 출력
print(words_dict.get(search_word, "없음"))