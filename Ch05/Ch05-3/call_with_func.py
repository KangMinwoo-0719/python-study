def power(item):
    return item * item

def under_3(item):
    return item < 3


list_input_a = [1, 2, 3, 4, 5]

# map 함수 사용
output_a = map(power, list_input_a)

# map() >> 리스트의 요소를 함수에 넣고
# 리턴된 값으로 새로운 리스트 구성

print(" # map() 함수 실행 결과 : ")
print(f"map (power, list_input_a) : {output_a}")
print(f"map (power, list_input_a) : {list(output_a)}")
print()


# filter 함수 사용
output_b = filter(under_3, list_input_a)

# filter() >> 리스트의 요소를 함수에 넣고 return 값이 True인 것으로
# 새로운 리스트 구성해 주는 함수

print(" # filter() 함수 실행 결과 : ")
print(f"map (under_3, list_input_a) : {output_b}")
print(f"map (under_3, list_input_a) : {list(output_b)}")