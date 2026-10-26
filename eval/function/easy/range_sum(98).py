def range_sum(num, start=1):
    """
    정수 num과 시작값 start를 입력받아
    start부터 num까지 정수의 합을 반환하는 함수

    Args: num -> int, start -> int
    Returns: int
    """

    # start부터 num까지 반복하여 합 누적 후 반환
    return sum(val for val in range(start, num + 1))

# 한 줄을 공백으로 나눕니다. 첫 토큰=n, 둘째 토큰(있으면)=start. 토큰 1개면 start 는 기본값 1. (정수)
parts = input().split()
num = int(parts[0])

# parts의 길이가 2면 start값 = parts[1], 없을 경우 기본값 1
start = int(parts[1]) if len(parts) == 2 else 1

# 함수 호출 후 반환값 출력
print(range_sum(num, start))