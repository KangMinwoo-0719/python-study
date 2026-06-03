# 모음 set 생성
vowels = {'a', 'e', 'i', 'o', 'u'}

# 입력받은 문자열 중 set에 포함된 문자는 제외하고 생성
result = ''.join(char for char in input() if char.lower() not in vowels)

# 결과값 출력
print(result)