string = input()

def reverse(string):
    """
    문자열(string)을 입력받아
    앞뒤를 전환한 문자열을 반환하는 함수

    Args: str(string)
    Returns: str
    """
    return string[::-1]

# 함수 호출 후 반환값 출력
print(reverse(string))