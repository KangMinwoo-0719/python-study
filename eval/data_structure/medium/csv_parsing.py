line = input()

# 입력받은 문자열을 ","(콤마)을 기준으로 이름, 나이, 점수로 구분하기
name, age, score = line.split(",")

# 구분한 각 변수 출력
print(f"이름: {name}")
print(f"나이: {age}")
print(f"점수: {score}")