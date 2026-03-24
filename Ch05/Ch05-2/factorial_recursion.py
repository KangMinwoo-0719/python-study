def factorial(n):

    if n == 0:
        return 1
    
    else:
        return n * factorial(n - 1)
    
num = int(input("정수 하나 입력 : "))
print(factorial(num))