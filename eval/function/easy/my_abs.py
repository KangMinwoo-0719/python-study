def my_abs(num):
    '''
    입력받은 정수를 음수면 양수, 양수면 그대로 반환하는 함수

    args : 정수형(int) 이면서 양수이거나 음수
    return : 정수형(int) 이면서 양수만 반환
    '''

    # 음수인 경우 양수로 변환
    if num < 0:
        num = -(num)

    # 변환값 또는 그대로 반환
    return num


num = int(input())

# 함수 호출 후 반환값 출력
print(my_abs(num))