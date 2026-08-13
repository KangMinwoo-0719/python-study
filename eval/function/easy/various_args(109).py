nums = [int(x) for x in input().split()]

def count_args(*args):
    """
    가변 매개변수(*args)에 입력받은
    인자값들의 개수를 반환하는 함수

    count_args(10, 20, 30)      -> 3

    Args: list(nums[int])
    Returns: int
    """
    return len(args)

# ↓ 호출부 (수정하지 마세요)
print(count_args(*nums))