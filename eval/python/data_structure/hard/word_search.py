docs = [
    "the cat sat on the mat",
    "the dog jumped over the cat",
    "python is fun",
    "i love programming",
    "the quick brown fox",
]
query = input()

# 컴프리헨션으로 리스트 생성
result = [index for index, doc in enumerate(docs) if query in doc.split()]

# 찾으면 인덱스 번호, 못 찾으면 없음 출력
if result:
    print(*result)
else:
    print("없음")