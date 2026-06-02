labels = ["cat", "dog", "bird", "fish", "lion"]
n = int(input())

# label의 값에 인덱스 번호를 부여하여 dict 생성
result = {kind: index for index, kind in enumerate(labels[:n])}

# 생성된 딕셔너리 순회하며 출력
for key, val in result.items():
    print(f"{key}: {val}")