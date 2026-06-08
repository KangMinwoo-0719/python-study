blood = input()
flag = False
msg = ''

# AB형 타입 출력
if blood == "AB":
    msg = "이성적이고 독창적인 성격"

# A형 타입 출력
elif blood == "A":
    msg = "꼼꼼하고 신중한 성격"

# B형 타입 출력
elif blood == "B":
    msg = "자유롭고 창의적인 성격"

# O형 타입 출력
elif blood == "O":
    msg = "사교적이고 리더십이 강한 성격"

# 예외처리
else:
    flag = True
    print("잘못된 입력입니다.")

if not flag:
    # 혈액형 출력
    print(f"혈액형: {blood}형")
    print(f"성격: {msg}")