# 가변 매개변수

def print_n_times(n, *values):

    for i in range(n):

        for value in values:

            print(value)

        print()

print_n_times(3, '안녕하세요', '가변', '매개함수')