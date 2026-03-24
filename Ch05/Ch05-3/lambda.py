# 함수 선언
power = lambda x : x * x
under_3 = lambda x : x < 3


# 리스트 변수 선언하기
list_input_a = [1, 2, 3, 4, 5]

# map 함수 사용하기
output_a = map(power, list_input_a)
print(output_a)
print(list(output_a))


# filter 함수 사용하기
output_b = filter(under_3, list_input_a)
print(output_b)
print(list(output_b))