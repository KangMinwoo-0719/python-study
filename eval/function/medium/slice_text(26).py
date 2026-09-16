parts = input().split()
text = parts[0]
start = int(parts[1])
end = int(parts[2])

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def slice_text(text, *, start, end):
    return text[start:end]

# 함수 호출 후 문자, 시작 문자열 인덱스, 끝 문자열 인덱스, 종료 지점 넘겨준 후
# 반환값 출력
print(slice_text(text, start=start, end=end))