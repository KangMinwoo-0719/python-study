def sec_to_str(sec):
    """
    정수 sec를 입력받아
    분, 초 단위로 변경 후 문자열로 반환하는 함수
    """

    # 입력받은 초(sec)를 분 단위로 계산 후 반환
    minute = sec // 60
    second = sec % 60
    return f"{minute}분 {second}초"

# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "130" 이면 sec == 130
sec = int(input())

# 함수 호출 후 반환값 출력
print(sec_to_str(sec))