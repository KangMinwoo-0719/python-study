words = input().split()

# 문자열의 점수 기준이 될 알파벳 나열 순서
letters = "abcdefghijklmnopqrstuvwxyz"

# 문자열 리스트 순회:
for word in words:

    # 해당 단어를 순회하여 각 점수를 저장한 후 sum
    score = sum([letters.index(char) + 1 for char in word])

    # 단어: 점수 형식 출력
    print(f"{word}: {score}")