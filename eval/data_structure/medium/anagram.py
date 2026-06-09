word1 = input()
word2 = input()

# a와 b의 정렬이 같으면 anagram, 다른 경우 아님 출력
print("anagram" if sorted(word1) == sorted(word2) else "아님")