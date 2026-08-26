nums = [int(x) for x in input().split()]

def range_span(*nums):
    """
    정수 리스트(nums)를 입력받아
    최댓값 - 최솟값을 반환하는 함수

    range_span([3, 1, 4, 1, 5])         -> 4
    range_span([5])                     -> 0

    Args: nums(list[int])
    Returns: int
    """

    # 정수 리스트의 최댓값 - 최솟값 결과 반환하기
    return max(nums) - min(nums)

# ↓ 호출부 (수정하지 마세요)
print(range_span(*nums))