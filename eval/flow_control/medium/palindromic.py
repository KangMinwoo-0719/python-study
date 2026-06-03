text = input()

# 입력받은 텍스트를 역순 슬라이싱하여 reversed_text에 저장
reversed_text = text[::-1]

# 뒤집어도 같다면 회문 아니면 아니라고 출력
print(f"{text}은(는) 회문입니다!" if reversed_text == text else f"{text}은(는) 회문이 아닙니다.")