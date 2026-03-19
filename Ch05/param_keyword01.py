# 키워드 매개변수

def print_n_times(*values, n=2):

    for i in range(n):

        for value in values:
            print(value)

        print()

# n 매개변수의 이름을 지정해서 입력
print_n_times('안녕하세요', '키워드', '매개변수', n = 3)