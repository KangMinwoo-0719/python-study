parts = input().split()
values = parts[:-1]
sep = parts[-1]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def join_all(*values, sep):
    return sep.join(values)

# 함수 호출 후 values, sep 인자 전달
# 반환값 출력하기
print(join_all(*values, sep=sep))