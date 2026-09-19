parts = input().split()
threshold = int(parts[0])
nums = [int(x) for x in parts[1:]]

def count_above(threshold, *nums):
    """
    기준값(threshold), 정수 리스트(nums)를 받아
    기준값보다 큰 정수 개수를 반환하는 함수
    """
    return sum([1 for num in nums if num > threshold])

# ↓ 호출부 (수정하지 마세요) — threshold 는 위치 인자, 나머지는 * 로 풀어 전달
print(count_above(threshold, *nums))