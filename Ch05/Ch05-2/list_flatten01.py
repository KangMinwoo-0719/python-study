# list 평탄화 기능 함수 선언하기:
def flatten(data):

    # 함수 반환값 리스트 output 선언하기
    output = []

    # 함수 매개변수(data)를 꺼내오며 반복문 돌기:
    for items in data:

        # 만약 반복문 매개변수 type == list 라면:
        if type(items) == list:

            # output 변수에 값 할당하기
            output += flatten(items)

        # 아니라면:
        else:

            # output 변수에 반복문 매개변수값 append 하기
            output.append(items)

    # 함수값 리턴하기
    return output


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print(flatten(example))