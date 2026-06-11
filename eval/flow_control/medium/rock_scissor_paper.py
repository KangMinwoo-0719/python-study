user = int(input())
computer = 2

# 입력값 1 -> 가위: 패배
if user == 1:
    print("당신: 가위 / 컴퓨터: 바위")
    print("아쉽게도 졌습니다. 😢")

# 입력값 2 -> 바위: 무승부
elif user == computer:
    print("당신: 바위 / 컴퓨터: 바위")
    print("무승부입니다! 😐")

# 입력값 3 -> 보: 승리
elif user == 3:
    print("당신: 보 / 컴퓨터: 바위")
    print("축하합니다! 당신이 이겼습니다! 🎉")

# 예외처리
else:
    print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")