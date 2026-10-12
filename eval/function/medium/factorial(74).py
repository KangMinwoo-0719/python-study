def factorial(num):
    total = 1
    for val in range(1, num + 1):
        total *= val
    return total

# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "5" 이면 n == 5
num = int(input())

# 함수 호출 후 반환값 출력
print(factorial(num))