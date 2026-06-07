words = input().split()

# 현재 단어 리스트의 중복값 제거 후 개수 출력
set_words = set(words)
print(f"종류: {len(set_words)}")

# 리스트 정렬 후 언패킹 출력
print(*sorted(set_words))