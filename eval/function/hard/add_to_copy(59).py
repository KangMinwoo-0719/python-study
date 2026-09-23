# 정수 리스트 nums 를 읽습니다. 예: "1 2" → nums=[1, 2]
nums = [int(x) for x in input().split()]

def add_to_copy(nums):
    """
    정수 리스트 nums를 받아
    복사본 리스트에 정수 99를 추가하여 리스트를 반환하는 함수

    Args: list(nums[int])
    Returns: list
    """
    nums_copy = nums[:]
    nums_copy.append(99)
    return nums_copy
    
# 함수 호출 후 반환된 리스트 출력
print(add_to_copy(nums))

# 원본 리스트 출력
print(nums)