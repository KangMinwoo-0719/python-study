def bigger(num1, num2):
    """
    더 큰 값을 반환하는 함수
    """
    return max(num1, num2)

num1, num2 = [int(x) for x in input().split()]

# 함수 호출한 후 반환값 출력
print(bigger(num1, num2))