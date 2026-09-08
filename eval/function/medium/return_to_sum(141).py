
data = [int(x) for x in input().split()]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def total(*nums):
    s = 0
    for n in nums:
        s += n
    return s

# 함수 호출 후 반환값 출력
print(total(*data))