# 매개변수로 받은 함수 10번 호출하기
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("hello")


call_10_times(print_hello)
