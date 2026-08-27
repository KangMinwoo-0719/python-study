parts = input().split()
factor = int(parts[0])
nums = [int(x) for x in parts[1:]]

def sum_scaled(factor, *nums):
    """
    배수(factor)와 숫자 리스트(nums)를 받아
    factor * sum(nums)의 값을 반환하는 함수
    """

    # 배수 * 정수 리스트의 합 값을 반환하기
    return factor * sum(nums)

# ↓ 호출부 (수정하지 마세요) — factor 는 위치 인자, 나머지는 * 로 풀어 전달
print(sum_scaled(factor, *nums))