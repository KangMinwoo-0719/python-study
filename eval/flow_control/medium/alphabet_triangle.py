# chr(65)는 'A', chr(65+1)은 'B'입니다.
n = int(input())

# 알파벳 'A'부터 시작할 숫자 저장할 변수
alpha_num = 65

# 정수 n만큼 라인 출력을 위해 반복:
for line in range(1, n + 1):

    # 한 라인에서 알파벳 진행을 위한 중첩반복:
    for alp in range(line):

        # 알파벳 숫자 + alp 출력 후 끌어오기
        print(chr(alpha_num + alp), end = "")

    # 줄바꿈 출력
    print()