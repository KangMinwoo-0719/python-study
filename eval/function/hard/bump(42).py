def bump():
    """
    지역변수 count에 전역변수 step을
    대입 후 지역변수 count를 반환하는 함수

    Args: None
    Returns: int
    """

    # 지역변수 count에 전역변수 step 대입 후 반환
    count = step
    return count

# 전역 count = 첫 값, step = 둘째 값. 예: "100 5" → count=100, step=5
parts = input().split()
count = int(parts[0])
step = int(parts[1])

# 함수 2번 호출 후 반환값과 전역 count 변수 출력
print(bump())
print(bump())
print(count)