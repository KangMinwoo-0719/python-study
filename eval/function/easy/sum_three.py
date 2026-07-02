def sum_three(num1, num2, num3):

    """
    3개의 정수(int)를 입력받아 합을 반환하는 함수

    sum_three(3, 4, 5) -> 12

    args : int(양수 또는 음수나 0)
    return : int(양수 또는 음수나 0)
    """
    return num1 + num2 + num3


num1, num2, num3 = [int(x) for x in input().split()]


# 함수 호출 후 반환값 출력하기
print(sum_three(num1, num2, num3))