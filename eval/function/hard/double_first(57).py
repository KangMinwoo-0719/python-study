def double_first(nums):
    """
    정수 리스트 nums를 받아
    맨 앞 요소 값에 2를 곱한 리스트를 반환하는 함수

    Args: list(nums[int])
    Returns: list
    """

    nums[0] *= 2
    return nums

# 함수 호출 후 반환값 출력
print(double_first(nums))