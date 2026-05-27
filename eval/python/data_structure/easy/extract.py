scores = [85, 92, 78, 95, 88, 70, 100, 65, 82, 90]
start_index = int(input())
end_index = int(input())

# 리스트의 시작 인덱스 ~ 끝 인덱스 부분만 언패킹 출력
print(*scores[start_index : end_index])