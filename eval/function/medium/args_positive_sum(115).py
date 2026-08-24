nums = [int(x) for x in input().split()]

def sum_positive(*nums):
    """
    정수 리스트를 입력받아
    양수의 합을 반환하는 함수
    """
    return sum(num for num in nums if num > 0)

# ↓ 호출부 (수정하지 마세요)
print(sum_positive(*nums))