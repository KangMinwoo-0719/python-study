n = int(input())
present = 0
absent = 0

# n값 반복:
for _ in range(n):

    # 이름 입력받은 후 출결 상태 입력받기
    name = input()
    status = int(input())

    # 예외처리
    if status < 0 or status > 1:
        print("1(출석) 또는 0(결석)으로 입력해주세요.")
    
    else:
    # 출석(1)인 경우 present + 1
        if status == 1:
            print(f"{name} - 출석")
            present += 1

        # 결석(0)인 경우 absent + 1
        else:
            print(f"{name} - 결석")
            absent += 1

print("--- 출석 결과 ---")
print("출석:", present, "명")
print("결석:", absent, "명")