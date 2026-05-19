# 바깥 for문으로 줄, 안쪽 for문으로 별 개수를 제어하세요.
n = int(input())


# 정수 n만큼 라인출력을 위한 반복:
for line in range(1, n + 1): 

    # 한 라인에 별 하나씩 늘리며 출력
    print('*' * line)