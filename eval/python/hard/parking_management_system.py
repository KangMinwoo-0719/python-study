"""
TITLE: 주차장 관리 시스템
DIFFICULTY: hard
TAGS: simulation, menu, while, if
EVAL: stdio

DESCRIPTION:
주차장 관리 시스템을 구현하시오.
- 최대 주차: 10대, 초기: 0대, 시간당 요금 1000원, 총 수입 0원
- 메뉴 루프마다 다음 헤더 출력 후 메뉴 번호 입력:
```
===== 주차장 관리 =====
1. 입차
2. 출차
3. 현황 조회
4. 종료
```
동작:
- 입차(1): 만차면 `주차장이 만차입니다!`, 아니면 `차량이 입차되었습니다. (현재 주차: K/10대)`
- 출차(2): 주차된 차 없으면 `주차된 차량이 없습니다.`, 있으면 시간 입력 → 요금 = max(0, 시간)*1000, `주차 요금: F원`, `차량이 출차되었습니다. (현재 주차: K/10대)` (총 수입 누적)
- 조회(3): `현재 주차: K/10대`, `빈 자리: M대`, `총 수입: T원`
- 종료(4): `시스템을 종료합니다.` 출력 후 종료
- 그 외: `잘못된 메뉴입니다.`

각 처리 후(종료 제외) 빈 줄 하나 출력.
"""

# while True와 if/elif로 구현하세요.
parked = 0
max_cars = 10
total_income = 0
rate = 1000


# 조건이 참인 동안 계속 반복:
while True:

  # 헤더 출력
  print("===== 주차장 관리 =====")
  print("1. 입차")
  print("2. 출차")
  print("3. 현황 조회")
  print("4. 종료")

  # 정수 입력받기
  status = int(input())

  # 1(입차)을 입력받으면 조건 비교:
  if status == 1:

    # 주차된 차가 max cars 미만일 시:
    if parked < max_cars:
    
      # 차량 추가
      parked += 1

      # "차량이 입차되었습니다. (현재 주차: {parked}/10대)" 출력
      print(f"차량이 입차되었습니다. (현재 주차: {parked}/10대)")
    

    # 만차가 된 경우:
    elif parked == max_cars:

      # "주차장이 만차입니다!" 출력
      print("주차장이 만차입니다!")


  # 2(출차)를 입력받으면 조건 비교:
  elif status == 2:

    # 주차된 차(parked == 0)가 없으면:
    if parked == 0:

      # "주차된 차량이 없습니다." 출력
      print("주차된 차량이 없습니다.")

    # 주차된 차가 있다면(parked != 0):
    elif parked != 0:

      # 주차 시간 입력받기
      parked_time = int(input())

      # "주차 요금 : {rate * 시간}" 출력하기
      print(f"주차 요금: {rate * parked_time}원")

      # 수입 더하기
      total_income += rate * parked_time

      # 출차된 차량 빼기
      parked -= 1

      # "차량이 출차되었습니다. (현재 주차: {parked}/10대)" 출력하기
      print(f"차량이 출차되었습니다. (현재 주차: {parked}/10대)")

  # 3(현황 조회)을 입력받으면 조건 비교:
  elif status == 3:

    # "현재 주차: {parked}/10대" 출력
    print(f"현재 주차: {parked}/10대")

    # "빈 자리: {max_cars - parked}대" 출력
    print(f"빈 자리: {max_cars - parked}대")

    # "총 수입: {total_income}원" 출력
    print(f"총 수입: {total_income}원")

  # 4(종료)를 입력받으면:
  elif status == 4:

    # "시스템을 종료합니다." 출력
    print("시스템을 종료합니다.")
    
    # break
    break

  # 위 숫자 말고 다른 숫자를 받은 경우:
  else:

    # "잘못된 메뉴입니다." 출력
    print("잘못된 메뉴입니다.")
  
  # 메뉴가 하나 실행될때마다 공백 출력
  print()