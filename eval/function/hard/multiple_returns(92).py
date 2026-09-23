# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

def stats4(nums):
    """
    숫자 리스트(nums)를 받아
    최솟값, 최댓값, 합, 평균 리스트를 반환하는 함수

    Args: list(nums)
    Returns: list
    """
    nums_all = sum(nums)
    return [min(nums), max(nums), nums_all, nums_all // len(nums)]

# 함수 호출 후 반환된 리스트 언패킹 출력
print(*stats4(nums))