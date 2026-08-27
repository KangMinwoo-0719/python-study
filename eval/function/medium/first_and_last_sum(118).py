nums = [int(x) for x in input().split()]

def first_and_last_sum(*nums):
    """
    정수 리스트를 입력받아
    첫 번째 인자와 마지막 인자의 합을 반환하는 함수

    first_and_last_sum([1, 2, 3, 4])            -> 5
    first_and_last_sum([5])                     -> 10

    Args: list(int)
    Returns: int
    """

    # 리스트의 첫 번째 인자와 마지막 인자를 추출하여 합한 값을 반환
    return nums[0] + nums[-1]

# ↓ 호출부 (수정하지 마세요)
print(first_and_last_sum(*nums))