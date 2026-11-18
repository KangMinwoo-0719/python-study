def clamp(value, low=0, high=100):
    """
    정수 value를 받아 상한 초과인 경우 high, 하한 미만인 경우 low 값을 반환하는 함수
    """

    # value가 low 미만인 경우 low 반환
    if value < low:
        return low

    # value가 high 초과인 경우 high 반환
    elif value > high:
        return high

    # 그 외의 경우 value 반환
    return value

# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 low, high 가 기본값으로 채워집니다. (모두 정수)
parts = input().split()
num = int(parts[0])
# parts의 길이가 3인 경우 low, high 값 할당
if len(parts) == 3:
    print(clamp(num, int(parts[1]), int(parts[2])))

# parts의 길이가 2인 경우 low 값 할당
elif len(parts) == 2:
    print(clamp(num, int(parts[1])))

# 그 외의 경우 value 인자만 전달
else:
    print(clamp(num))