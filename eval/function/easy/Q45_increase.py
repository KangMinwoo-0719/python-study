def increase():
    """호출 될 때 마다 전역 변수 count를 1씩 증가시키는 함수"""
    # 전역변수 count + 1
    global count
    count += 1

count = 0

# 정수 입력받기
num = int(input())

# 입력받은 정수만큼 반복하여 함수 호출하기
for _ in range(num):
    increase()

# 전역변수 count 출력
print(count)