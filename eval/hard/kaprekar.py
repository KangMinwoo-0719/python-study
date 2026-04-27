# 1부터 N 사이의 카프리카 수를 찾아 출력하세요.
n = int(input())

# 리스트 형식으로 문자를 저장시킬 list
list_num = []

# 숫자를 저장할 변수
num = ''

# 카프리카 수 출력
print("카프리카 수:")

# 1부터 입력받은 n값 + 1 범위 반복:
for kaprekar in range(1, n + 1):

    # 1은 예외처리
    if kaprekar == 1:
        print(1)

    # 10 제곱단위도 예외처리
    elif kaprekar % 10 == 0:
        continue  

    # 숫자 제곱 후 문자열로 변환
    else:
        num = str(kaprekar ** 2)

        # 제곱 값이 81 미만이면 continue(이 아래는 카프리카 수 없음)
        if int(num) < 81:
            continue

        # 문자열을 하나씩 돌기:
        for char in num:

            # 리스트에 문자로 하나씩 추가하기
            list_num.append(char)

        # 리스트 요소, 인덱스 가져오기
        for index, num_2 in enumerate(list_num, 1):

            # 오른쪽 문자열 숫자를 저장할 변수
            right_num = ''

            # 왼쪽 숫자들부터 하나씩 가져와 저장한 후 비교
            left_num += num_2

            # 오른쪽 숫자 저장하기 위한 반복
            for num_3 in range(index, len(list_num)):

                right_num += list_num[num_3]

            # 오른쪽 값이 공백이면 반복 중단
            if right_num == '':
                break

            # 분리한 숫자 + 나머지 숫자의 합이 현재의 수와 같으면 출력(카프리카 수)
            elif int(left_num) + int(right_num) == kaprekar:
                print(f"{kaprekar}: {kaprekar}^2 = {num}, {left_num} + {right_num} = {kaprekar}")

                # 찾으면 현재 반복 중단
                break

    # 리스트, 왼쪽에서부터 저장했던 숫자 리셋
    left_num = ''
    list_num.clear()