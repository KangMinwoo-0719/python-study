parts = input().split()
title = parts[0]
values = [int(x) for x in parts[1:]]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def summary(title, *nums):
    s = 0
    for n in nums:
        s += n
    return title + ": " + str(s)

# summary 함수를 호출하여 인자값 title, values를 넘겨준 후 반환값 출력
print(summary(title, *values))