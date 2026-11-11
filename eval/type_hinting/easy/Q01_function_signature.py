from typing import get_type_hints

# 첫 줄: "단어 횟수" (예: "ha 3" -> word="ha", times=3). 둘째 줄: "a b" 정수 두 개. 셋째 줄: 나이 정수
word, times = input().split()
times = int(times)
a, b = map(int, input().split())
age = int(input())


def repeat(word: str, times: int) -> str:      # 완성된 예시 — 매개변수 힌트 + 반환 힌트
    return word * times

def average(a: int, b: int) -> float:
    """나이의 평균 값을 반환하는 메서드"""
    return (a + b) / 2

def is_adult(age: int) -> bool:
    """나이가 19세 이상인지 미만인지 확인 후 boolean 타입을 반환하는 함수"""
    return True if age >= 19 else False

# ---- 호출부 (수정 금지) ----
print(repeat(word, times))
print(average(a, b))
print(is_adult(age))
h = get_type_hints(repeat)
print(h.get("word") is str, h.get("times") is int, h.get("return") is str)
h = get_type_hints(average)
print(h.get("a") is int, h.get("b") is int, h.get("return") is float)
h = get_type_hints(is_adult)
print(h.get("age") is int, h.get("return") is bool)
x: int = "hello"            # 힌트와 다른 타입을 넣어도 오류 없이 실행된다 (힌트는 강제가 아님)
print(type(x).__name__)