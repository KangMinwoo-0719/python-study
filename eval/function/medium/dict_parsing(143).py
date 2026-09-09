# key=value 토큰을 dict 로 파싱합니다. 예: "name=철수 age=20 city=서울" → opts={"name":"철수","age":"20","city":"서울"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def profile(name, age, city):
    return name + "/" + age + "/" + city

# 함수 호출 후 반환값 출력
print(profile(**opts))