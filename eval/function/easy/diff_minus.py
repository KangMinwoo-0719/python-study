def difference(num1, num2):

    """
    정수(int)를 2개 받아, 들어온 순서의 차(첫 째 - 둘 째) 값 반환

    difference(4, 5) -> -1

    args : int(양수 혹은 음수 또는 0)
    return : int(양수 혹은 음수 또는 0)
    """
    return num1 - num2

# 각각의 정수를 입력받은 후 저장
num1, num2 = [int(x) for x in input().split()]

# 함수 호출 후 반환값 출력
print(difference(num1, num2))