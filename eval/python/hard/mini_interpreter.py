# 미니 인터프리터: SET, ADD, PRINT 명령어를 처리하세요.
n = int(input())
x = 0
y = 0
char = ''
char_to_int = 0
# n값 만큼 반복:
for _ in range(n):

    # 명령어 문자열로 입력받기
    command = input()

    # 맨 뒷자리 문자열이 숫자가 아니면서 PRINT 명령어인 경우:
    if 'PRINT' in command:
        if 'x' in command:
            print(x)
        elif 'y' in command:
            print(y)

    else:

        # 맨 뒤에서 2번째 자리도 숫자면 2의 자리 수
        if command[-2] == " ":
            char_to_int = int(command[-1])
        else:
            char = command[-2] + command[-1]
            char_to_int = int(char)


        # 변수가 x인 경우:
        if 'x' in command:

            # 명령어가 SET이면 x 변수에 값 저장
            if 'SET' in command:
                x = char_to_int

            # ADD이면 값 누적
            elif 'ADD' in command:
                x += char_to_int

            # 명령어 예외처리
            else:
                print("SET / ADD / PRINT 중 입력하세요.")

        # 변수가 y인 경우:
        elif 'y' in command:

            # 명령어가 SET이면 y 변수에 값 저장
            if 'SET' in command:
                y = char_to_int

            # ADD이면 값 누적
            elif 'ADD' in command:
                y += char_to_int

            # 명령어 예외처리
            else:
                print("SET / ADD / PRINT 중 입력하세요.")

        # 변수 예외처리
        else:
            print("x 또는 y를 입력하세요.")
