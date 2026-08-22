nums = [int(x) for x in input().split()]

def count_even(*nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1

    return count

# ↓ 호출부 (수정하지 마세요)
print(count_even(*nums))