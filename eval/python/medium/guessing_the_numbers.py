# while True 안에서 정답일 때 break 하세요.
answer = 42

# 참일 동안 반복:
while True:

    # 정답 입력받기
    guess_num = int(input())

    # 일치하면 "정답입니다!" 출력 후 break
    if guess_num == answer:
        print("정답입니다!")
        break

    # 정답보다 크면 작은 수 입력하라는 문구 출력
    elif guess_num > answer:
        print("더 작은 수를 입력하세요")

    # 정답보다 작으면 큰 수 입력하라는 문구 출력
    else:
        print("더 큰 수를 입력하세요")