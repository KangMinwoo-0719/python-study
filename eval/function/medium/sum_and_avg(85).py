def sum_avg(nums):
    """
    정수 리스트 nums를 입력받아
    합과 개수를 반환하는 함수

    Args: list -> nums[int]
    Returns: tuple -> (int, int)
    """

    # 정수 리스트의 합과 평균(정수)을 구한 후 반환하기
    nums_sum = sum(nums)
    nums_avg = nums_sum // len(nums)

    return nums_sum, nums_avg
# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 함수 호출 후 값 언패킹
summary, avg = sum_avg(nums)

# 합과 평균 출력
print(summary, avg)