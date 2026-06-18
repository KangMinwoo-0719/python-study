num = int(input())

# 입력받은 숫자 문자열로 변경
str_num = str(num)
count = 0

# 디지털 근 길이가 2보다 작아지면 종료:
while len(str_num) > 1:
    count += 1

    # 숫자를 돌며 정수형으로 변환 후 값 누적
    digital_root = sum(int(number) for number in str_num)

    # 각 단계 자릿수 합 출력
    print(f"단계 {count}: 자릿수 합 계산 {'+'.join(str_num)} → {digital_root}")

    # 디지털 근 갱신
    str_num = str(digital_root)
    
# 디지털 근 출력
print(f"디지털 근: {str_num}")