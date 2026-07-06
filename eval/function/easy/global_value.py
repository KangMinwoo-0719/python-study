def announce():
    """
    문자열(str)을 받아 "[공지]" 문자열을 덧붙인 후 반환하는 함수

    args : -
    return : str
    """
    return "[공지] " + message

# 전역변수 message 를 입력에서 읽습니다. 예: "회의 3시" → message="회의 3시"
message = input()

# 함수 선언 후 반환값 출력
print(announce())