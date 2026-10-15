def stats(nums):
    """
    정수 리스트 nums를 받아
    최솟값, 최댓값, 합 세 값을
    공백을 기준으로 나누어 반환하는 함수

    Args: list -> nums[int]
    Returns: tuple -> (int, int, int)
    """ 

    # nums 리스트의 최솟값, 최댓값, 합 계산
    nums_max = max(nums)
    nums_min = min(nums)
    nums_sum = sum(nums)

    # 구한 세 값 반환
    return nums_max, nums_min, nums_sum

# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 호출 후 값 언패킹
maximum, minimum, summary = stats(nums)

# 언패킹 값 출력
print(minimum, maximum, summary)