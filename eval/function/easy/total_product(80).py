def sum_product(a, b):
    """
    a(int), b(int) 두 정수를 받아
    합과 곱을 반환하는 함수

    sum_product(3, 5) -> (8, 15)

    args: a(int), b(int)
    returns: tuple(합(int), 곱(int))
    """
    return a + b, a * b

# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "3 5" → a=3, b=5
a, b = [int(x) for x in input().split()]

# 함수 호출 후 반환된 튜플 언패킹
summary, time = sum_product(a, b)

# 합과 곱 출력
print(summary, time)