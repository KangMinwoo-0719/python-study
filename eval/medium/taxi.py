# 거리 계산 후 야간 여부를 추가 판단하세요.
distance = float(input())
hour = int(input())

# 기본 요금
normal_price = 4800

# 야간 요금 저장할 변수
night_price = 0

# 추가 요금 저장할 변수
add_charge = 0

# 총합 요금을 저장할 변수
total_price = 0


# 기본요금 출력
print(f"기본요금: {normal_price}원")

# 거리가 2키로미터 초과인 경우 추가요금 부과:
if distance > 2:

    add_charge = int((distance - 2) * 1000)
    total_price = add_charge + normal_price

# 초과하지 않은 경우 기본값 저장
else:
    total_price += normal_price

print(f"추가요금: {add_charge}원")

#시간대가 22 이상 6 미만인 경우 야간할증 추가(거리는 기본요금)
if hour >= 22 or hour < 6:
    night_price = int(total_price * 0.2)
    total_price += + night_price
    print(f"야간 할증 (20%): {night_price}원")


# 최종 금액 출력
print(f"총 택시비: {total_price}원")