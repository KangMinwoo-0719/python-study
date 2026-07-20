def describe():
    """
    매개변수 없이 전역변수 name(str), age(str)
    -> "name(age)" 형식으로 바꾸어 반환하는 함수

    describe(), name = '철수', age = 20 -> "철수(20)"

    args: None
    returns: str(name(age))
    """
    return f"{name}({age})"

# 전역 name = 첫 단어, age = 둘째 단어. 예: "철수 20" → name="철수", age="20"
parts = input().split()
name = parts[0]
age = parts[1]

# 함수 호출 후 반환값 출력
print(describe())