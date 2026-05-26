# 3개 문장을 라운드별로 처리하세요.
text1 = "Hello Python"
text2 = "I love coding"
text3 = "Practice makes perfect"

total_correct = 0
total_chars = 0
round_num = 1

# 텍스트 딕셔너리로 저장
text_dict = {
    "text1" : "Hello Python",
    "text2" : "I love coding",
    "text3" : "Practice makes perfect"
}

# 문장 검사하는 함수 선언:
def inspection_acc(text, vals):

    # 문자열 검사를 위해 임의 지정하는 정수
    num = 0

    # 맞는 문자열 저장하기 위한 변수
    correct = 0

    # 입력받은 문자열 값 하나씩 돌기:
    for word in text:

        # text[n]번 문자열과 같으면 correct + 1
        if vals[num] == word:

            correct += 1

        # num값 1씩 올리기
        num += 1

    # 값 리턴
    return correct
        

# 전체 문자열 저장하기
total_chars += len(text1) + len(text2) + len(text3)


# 타자 연습 시작을 알리는 문구 출력
print("=== 타자 연습 ===")
print("표시된 문장을 정확히 입력하세요!")

# 딕셔너리의 value, key 값 가져오기
for text_key, text_val in text_dict.items():

    print()

    # 1번 문장 출력 후 입력받기
    test = input(f"[{round_num}번 문장] {text_val}")
    
    print()

    # 만약 텍스트 입력값이 정답 텍스트보다 길면 에러처리
    if len(test) > len(text_val):
        print("비교 안 됨")

    # 정상인 경우 정확도 계산 후 출력
    else:
        correct = inspection_acc(test, text_val)
        print(f"정확도: {(int((correct / len(text_val) * 100) * 10) / 10)}% ({correct}/{len(text_val)} 글자)")

        # 함수 선언 후 총합 total에 값 더하기
        total_correct += inspection_acc(test, text_val)

    # 라운드 증가
    round_num += 1


# 최종 결과, 전체 정확도, 총 글자 수 출력
print()
print("=== 최종 결과 ===")
total_acc = (int(((total_correct / total_chars) * 100) * 10) / 10)
print(f"전체 정확도: {total_acc}% ({total_correct}/{total_chars} 글자)")