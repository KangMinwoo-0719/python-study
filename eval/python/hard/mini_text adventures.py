# while game_over == 0 루프에서 current_room으로 분기
hp = 100
has_key = 0
current_room = 1
game_over = 0

# 게임 시작 문구 출력
print("=== 미니 텍스트 어드벤처 ===")
print("당신은 신비한 던전에 들어왔습니다...")
print(f"HP: {hp}")


# 게임오버가 1이 될 때까지 계속 반복:
while game_over == 0:

  print()

  # 현재 방 번호가 1이면:
  if current_room == 1:

    # 시작의 방 임을 알리는 문구와 두 개의 문 선택지 출력
    print("--- 방 1: 시작의 방 ---")
    print("두 개의 문이 보입니다.")
    print("(1) 왼쪽 문  (2) 오른쪽 문")

    # 정수로 1 또는 2를 입력받기
    room_1_num = int(input()) 

    # 왼쪽(1)을 선택하면 아래 문구 출력
    if room_1_num == 1:
      print("왼쪽 문을 열고 조심스럽게 들어갑니다.")
      current_room += 1

    # 오른쪽(2)을 선택하면 hp -20:
    elif room_1_num == 2:
  
      # 함정 발동과 hp 절감 문구 출력
      print("오른쪽 문에 함정이 있었습니다! HP -20")
      hp -= 20
      print(f"HP: {hp}")
      current_room += 1

    # 1 또는 2 이외의 선택지 입력 시 아래 문구 출력
    else:
      print("1 또는 2를 선택하세요.")
    

  # 현재 방 번호가 2면:
  elif current_room == 2:

    # 보물 방 임을 알리는 문구 출력
    print("--- 방 2: 보물의 방 ---")
    print("낡은 상자가 하나 있습니다.")
    print("(1) 상자 열기  (2) 그냥 지나가기")

    # 1(상자 열기) 또는 2(지나가기) 정수를 입력받기
    room_2_num = int(input())

    # 1을 선택했다면 열쇠 획득 문구 출력:
    if room_2_num == 1:
      print("상자에서 열쇠를 발견했습니다!")
      current_room += 1

      # 열쇠 + 1
      has_key = 1

    # 2를 선택했다면 아래 문구 출력
    elif room_2_num == 2:
      print("상자를 무시하고 지나갑니다.")
      current_room += 1
    
    # 1 또는 2 이외의 입력 시 아래 문구 출력
    else:
      print("1 또는 2를 선택하세요.")

  
  # 현재 방 번호가 3이면:
  elif current_room == 3:

    # 최종 방을 알리는 문구 출력
    print("--- 방 3: 최종 방 ---")
    print("거대한 잠긴 문이 보입니다.")

    # 만약 열쇠가 있다면(key == 1이라면):
    if has_key == 1:

      # 열쇠로 문을 열었다는 문구 출력
      print("열쇠로 문을 열었습니다!")
      print()
      # 던전 탈출 문구 출력
      print("축하합니다! 던전에서 탈출했습니다!")
      print(f"남은 HP: {hp}")

      # break
      game_over += 1

    # 열쇠가 없다면:
    else:

      # 1(2번 방 돌아가기) 또는 2(문 부수가) 정수로 입력받기
      print("문이 잠겨 있습니다! 열쇠가 필요합니다. ")
      print("(1) 돌아가기(방2) (2) 문 부수기(HP-50)")
      print()
      room_3_num = int(input())

      # 1을 선택하면 방 번호 - 1하여 2번 방으로 돌아가기:
      if room_3_num == 1:
        print("방 2로 돌아갑니다.")
        print()
        current_room -= 1

      # 2를 선택하면 hp -50 절감:
      elif room_3_num == 2:
        print("문을 부쉈습니다! HP -50")
        hp -= 50
        print(f"HP: {hp}")
        
        # hp가 0이 되면 게임 오버 출력:
        if hp <= 0:
          print("체력이 다했습니다... 게임 오버!")
        
        # hp가 0 초과라면 탈출 성공:
        elif hp > 0:
          print("문을 부수고 탈출했습니다!")
          print(f"남은 HP: {hp}")
        
        # 게임 종료
        game_over += 1

      # 1 또는 2 이외의 선택지 입력 시 아래 문구 출력
      else:
        print("1 또는 2를 선택하세요")