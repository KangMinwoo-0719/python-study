nums = [int(x) for x in input().split()]

def product_all(*nums):
    """
    정수 리스트(nums)를 받아
    모두 곱한 값을 반환하는 함수
    """

    total = 1

    # 정수 리스트를 순회하며 곱 누적 후 반환
    for num in nums:
        total *= num

    return total

# ↓ 호출부 (수정하지 마세요)
print(product_all(*nums))