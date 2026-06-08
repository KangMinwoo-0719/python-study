start = int(input())
stop = int(input())
step = int(input())

# start ~ stop 범위를 step만큼 뛰어넘으며 저장
result = [str(num) for num in range(start, stop, step)]

# 공백을 중간에 두고 출력
print(" ".join(result))