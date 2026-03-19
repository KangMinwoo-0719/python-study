# 기본 매개변수


# n의 값이 주어지지 않으면 기본값은 2가 됨
def print_n_times(value, n = 2):
    for i in range(n):
        print(value)

print_n_times("안녕하세요")