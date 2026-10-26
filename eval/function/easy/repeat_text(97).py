def repeat_text(text, times=2):
    """
    문자열(text), 반복 횟수(times)를 받아
    문자열 * 반복 횟수 문자열 값을 반환하는 함수
    """

    return text * times

# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 2회, 2개면 둘째 값(정수)이 반복 횟수입니다.
parts = input().split()
text = parts[0]
if len(parts) == 2:
    times = int(parts[1])
    print(repeat_text(text, times))

else:
    print(repeat_text(text))