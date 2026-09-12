# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4 5" → nums=[1, 2, 3, 4, 5]
nums = [int(x) for x in input().split()]

# TODO: 여기에 함수 trimmed_sum(*nums) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def trimmed_sum(*nums):
    """
    nums 리스트를 받아
    전체 합에서 최대값과 최소값을 제외한 값을
    반환하는 함수
    """

    # 최대값과 최소값을 제외한 전체 합 반환
    return sum(nums) - max(nums) - min(nums)

# ↓ 호출부 (수정하지 마세요)
print(trimmed_sum(*nums))