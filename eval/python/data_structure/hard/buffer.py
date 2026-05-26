k = int(input())
buffer_size = []

# END를 입력받기 전 까지 무한 반복:
while True:

    # 문자열 입력받기
    command = input()

    # END를 입력받으면 종료
    if command == "END":
        break

    buffer_size.append(command)

    # list 길이가 버퍼값(k)를 초과하면 list의 0번째 인덱스 삭제(최신화)
    if len(buffer_size) > k:
        buffer_size.pop(0)

# list 언패킹 출력
print(*buffer_size)