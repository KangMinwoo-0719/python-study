opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

def greet(greeting, name):
    return greeting + ", " + name + "!"

# 함수 호출 후 opts 딕셔너리를 언패킹 후 인자값 전달, 반환값 출력
print(greet(**opts))