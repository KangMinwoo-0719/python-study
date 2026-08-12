# 총 초를 입력받아 HH:MM:SS 형식으로 출력하세요.
total_sec = int(input())

# 시간 계산
hour = total_sec // 3600

# 분 계산
minute = (total_sec % 3600) // 60

# 초 계산
second = total_sec % 60

# 디지털 시계로 반환한 값 출력
print(f"{hour:02d}:{minute:02d}:{second:02d}")