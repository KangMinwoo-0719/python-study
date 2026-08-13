def greet(name, greeting="안녕하세요"):
    """
    이름(name), 인사말(greeting)을 입력받아
    greeting, name님! 형식으로 출력하는 함수

    greet("철수")           -> 안녕하세요, 철수님!

    Args: name(str), greeting(str)
    Returns: None
    """
    print(f"{greeting}, {name}님!")

# 한 줄을 공백으로 나눕니다. 예: "철수" → ["철수"](기본값 사용) / "철수 반가워" → ["철수","반가워"](override)
parts = input().split()

greet(*parts)