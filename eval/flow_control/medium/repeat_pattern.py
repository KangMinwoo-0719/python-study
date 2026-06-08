text = input()
n = int(input())

# 문자열 순회:
for char in text:

    # 현재 문자열 * n 출력 후 끌어오기
    print(char * n, end="")

# 마지막 줄바꿈
print()