# 플레이어 HP와 몬스터 HP를 입력받아 턴제 전투를 시뮬레이션하세요.
player_hp = int(input())
monster_hp = int(input())

# 턴 수를 저장할 변수 turn
turn = 0


# 전투 시작을 알리는 문구와 플레이어, 몬스터 hp 동시 출력
print("=== RPG 전투 시작! ===")
print(f"플레이어 HP: {player_hp} | 몬스터 HP: {monster_hp}")

# True일 동안 반복:
while True:

    print()

    # 플레이 턴 + 1
    turn += 1

    # 플레이어의 데미지를 저장할 변수
    player_damage = 15 + (turn * 7 + 3) % 11

    # 몬스터의 데미지를 저장할 변수
    mon_damage = 10 + (turn * 13 + 5) % 11


    # --- n턴 --- 출력
    print(f"--- {turn}턴 ---")

    # "플레이어 공격!" 문구 출력 후 데미지, 공격 후 남은 몬스터 hp 출력
    # 몬스터 HP 감소
    monster_hp -= player_damage
    print(f"플레이어 공격! 데미지: {player_damage} | 몬스터 HP: {monster_hp}")

    # 몬스터 체력 <= 0이 되면 플레이어 승리, (n턴 만의 승리) 문구 출력 후 break
    if monster_hp <= 0:
        print()
        print(f"플레이어 승리! ({turn}턴 만에 승리)")
        break


    # 플레이어 HP 감소
    # "몬스터 공격!" 문구 출력 후 데미지, 공격 후 남은 플레이어 hp 출력
    player_hp -= mon_damage
    print(f"몬스터 공격! 데미지: {mon_damage} | 플레이어 HP: {player_hp}")
    
    # 플레이어 체력 <= 0이 되면 몬스터 승리, "플레이어 패배 문구" 출력 후 break
    if player_hp <= 0:
        print()
        print("몬스터 승리... (플레이어 패배)")
        break