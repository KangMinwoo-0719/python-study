# 메모 변수 할당
dict_a = {
    1 : 1,
    2 : 1
}

# 피보나치 함수 선언
def fibonacci(n):
    if n in dict_a:

        return dict_a[n]
    
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dict_a[n] = output
        return output

print(fibonacci(10))