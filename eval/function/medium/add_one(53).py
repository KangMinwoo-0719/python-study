# 정수 x 를 입력에서 읽습니다. 예: "10" → x=10
x = int(input())

# TODO: add_one(n) 을 정의하고, add_one(x) 반환값과 원본 x 를 두 줄로 print 하세요.
def add_one(n):
    """
    매개변수 n을 받아 n + 1값을 반환하는 함수
    """
    return n + 1

# 함수 호출 후 반환값 출력
print(add_one(x))
print(x)