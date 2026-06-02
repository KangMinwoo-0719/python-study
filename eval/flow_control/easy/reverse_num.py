num = int(input())
reverse = 0

# 입력받은 문자열을 다 뒤집을때까지 반복:
while num > 0:

    # 맨 뒷자리 숫자부터 하나씩 분리
    digit = num % 10

    # 뒤집은 숫자를 새로운 변수에 맨 앞부터 할당
    reverse = reverse * 10 + digit

    # 현재 입력받은 숫자에서 뒷자리씩 제거
    num //= 10

# 뒤집은 숫자 출력
print(f"뒤집은 숫자: {reverse}")