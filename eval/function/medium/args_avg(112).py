nums = [int(x) for x in input().split()]

def average_args(*nums):
    """
    nums 리스트의 인자 총 합 // 개수 값을
    반환하는 함수
    """
    return sum(nums) // len(nums)

# ↓ 호출부 (수정하지 마세요)
print(average_args(*nums))