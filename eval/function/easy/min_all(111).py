nums = [int(x) for x in input().split()]

def min_all(*nums):
    """
    정수 리스트(nums)를 받아
    가장 작은 정수 값을 반환하는 함수

    min_all([3, 1, 4, 1, 5])        -> 1
    min_all([5])                    -> 5

    Args: nums(list[int])
    Returns: int
    """
    return min(nums)

# ↓ 호출부 (수정하지 마세요)
print(min_all(*nums))