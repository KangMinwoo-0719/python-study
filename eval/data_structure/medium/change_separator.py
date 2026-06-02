text = input()
new_sep = input()

# text를 콤마 기준으로 분리
parts = text.split(",")

# 분리한 text를 new_sep으로 join 후 저장
result = new_sep.join(parts)

# 결과값 출력
print(result)