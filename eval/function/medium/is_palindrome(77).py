string = input()


def is_palindrome(string):
    """
    문자열 string을 입력받아
    앞뒤를 뒤집었을 때 똑같은 문자열인 경우 True,
    아닌 경우 False를 반환하는 함수

    Args: str(string)
    Returns: boolean
    """
    return True if string == string[::-1] else False

# 함수 호출 후 반환값 출력
print(is_palindrome(string))