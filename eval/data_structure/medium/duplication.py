n = int(input())
found = False
seen = set()

# n값 범위 반복:
for _ in range(n):

    # 단어 입력받기
    word = input()

    # 입력받은 단어가 이미 set에 포함되어 있다면 현재 단어 출력 후 break
    if word in seen:
        print(word)
        found = True
        break

    # 없는 경우 저장
    else:
        seen.add(word)

# 중복이 없다면 중복 출력
if not found:
    print("중복 없음")