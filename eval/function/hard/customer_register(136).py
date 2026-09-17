opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

def register(name, **kwargs):
    """
    kwargs 인자를 받아 이름, 옵션 받아
    {name}: options 형식의 문자열을 반환하는 함수
    """

    # kwargs의 value값을 추출해 이름, 옵션 값 반환하기
    result = sorted(f"{key}={value}" for key, value in kwargs.items())
    return f"{name}: {','.join(result)}"


# ↓ 호출부 (수정하지 마세요) — name 은 name 매개변수로, 나머지는 **options 로 모임
print(register(**opts))