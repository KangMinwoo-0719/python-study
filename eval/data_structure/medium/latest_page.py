items = input().split()
# 둘째·셋째 줄: int(input()) 으로 정수 하나씩 읽기
item_len = int(input())
page = int(input())
result = []

# 입력받은 게시물 최신화(뒤집기)하기
update_items = items[::-1]

# 보여줄 글 수 크기만큼 step 지정 후 반복:
for idx in range(0, len(update_items), item_len):

    # 최신화 된 게시물을 보여줄 글 수 만큼 슬라이싱 후 저장
    result.append(list(item for item in update_items[idx:idx+item_len]))

# 출력 할 페이지가 최신화 된 결과의 길이보다 길면 빈 페이지 출력
if page > len(result):
    print("빈 페이지")

# 슬라이싱하여 저장한 리스트에서 볼 페이지(인덱스 - 1) 값 언패킹 출력
else:
    print(*result[page - 1])