def to_hms(sec):
    """
    전체 초(sec)를 정수로 입력받아
    시, 분, 초 로 변환한 값을 반환하는 함수

    Args: int(sec)
    Returns: tuple -> (int, int, int)
    """

    # 입력받은 정수를 시, 분, 초 단위로 분리 후 반환
    hour = sec // 3600
    minute = (sec % 3600) // 60
    second = sec % 60
    return hour, minute, second

# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "3661" 이면 sec == 3661
sec = int(input())

# 함수를 호출 후 시, 분, 초 값을 언패킹 하여 받기
h, m, s = to_hms(sec)

# 시, 분, 초 순서대로 출력
print(h, m, s)