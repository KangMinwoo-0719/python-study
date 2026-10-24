def build_tag(name, level=1):
    """
    이름(name), 레벨(level)을 입력받아
    level * "#" + name 문자열을 반환하는 함수
    """
    # level * "#" + name 문자열 값 반환하기
    return level * "#" + name

# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 레벨(1), 2개면 둘째 값(정수)이 레벨입니다.
parts = input().split()
name = parts[0]
level = 1
if len(parts) == 2:
    level = int(parts[1])

# 함수 호출 후 반환값 출력
print(build_tag(name, level=level))