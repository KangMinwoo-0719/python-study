def count_vowels(string):
    """
    문자열 string을 입력받아
    모음(a, e, i, o ,u)이 포함되어 있으면
    모음의 개수를 반환하는 함수

    Args: str
    Returns: int
    """
    # 모음 집합 정의
    vowels = ("a", "e", "i", "o", "u")

    # 모음 개수 카운트 후 개수 반환
    return sum(1 for char in string if char in vowels)

# input() 으로 문자열 한 줄을 읽습니다. 예: 입력이 "hello" 이면 s == "hello"
string = input()

# 함수 호출 후 반환값 출력
print(count_vowels(string))