def first_exceed(nums, threshold):
    """
    정수 리스트 nums를 받아
    nums 리스트의 요소들 값을 누적하며 합해
    기준값 threshold를 처음으로 초과하는 경우 해당 인덱스, 다 더해도
    초과하지 못하는 경우 -1을 반환하는 함수

    Args: list -> nums[int]
    Returns: int
    """

    # 리스트와 인덱스(0부터 시작)를 동시 순회하며
    # 누적 합이 threshold를 처음 넘는 순간 현재 인덱스 번호 반환
    total = 0
    for idx, num in enumerate(nums, 0):
        total += num
        if total > threshold:
            return idx

    # 다 더해도 넘지 못하는 경우 -1 반환
    return -1
    
threshold = int(input())
nums = [int(x) for x in input().split()]

# 함수 호출 후 반환값 출력
print(first_exceed(nums, threshold))