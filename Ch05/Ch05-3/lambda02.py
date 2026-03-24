list_input_a = [1, 2, 3, 4, 5]


# lambda 함수를 매개변수에 바로 넣음
# map 함수 사용
output_a = map(lambda x : x * x, list_input_a)
print(output_a)
print(list(output_a))

# filter 함수 사용
output_b = filter(lambda x : x < 3, list_input_a)
print(output_b)
print(list(output_b))