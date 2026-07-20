allowed = {"apple", "banana", "cherry", "date", "fig"}
word_set = set()

# 입력받을 단어만큼 숫자 입력받기
word_count = int(input())

# word_count 수 만큼 반복:
for _ in range(word_count):

    # 단어 입력받은 후 집합에 추가
    word = input()
    word_set.add(word)


# 입력받은 단어 - allowed 결과 저장
result = word_set - allowed

# 차집합 결과가 False인 경우 모두 포함
if not result:
    print("모두 포함")

# 미포함 된 단어가 있는 경우 공백을 기준으로 나누어 정렬 출력
else:
    print(f"미포함: {' '.join(sorted(result))}")