player_hp = 100
monster_hp = 80
turn = 0
p_lose = False
print("=== RPG 전투 시작! ===")
print("플레이어 HP:", player_hp, "| 몬스터 HP:", monster_hp)
print()

# 플레이어, 몬스터 둘 중 하나의 hp가 0이 되기 전 까지 반복:
while True:

    # 현재 턴 출력
    turn += 1
    print(f"--- {turn}턴 ---")

    # 플레이어, 몬스터의 데미지
    player_damage = 15 + (turn * 7 + 3) % 11
    monster_damage = 10 + (turn * 11 + 5) % 11

    # 플레이어 선 공격 -> 데미지(15 + (turn * 7 + 3) % 11) 출력
    # 공격 후 몬스터의 남은 hp 출력
    monster_hp -= player_damage
    print(f"플레이어 공격! 데미지: {player_damage} | 몬스터 HP: {monster_hp}")

    # 몬스터 hp가 0 이하가 되면 플레이어 승리, break
    if monster_hp <= 0:
        break

    # 몬스터 후 공격 -> 데미지(10 + (turn * 11 + 5) % 11) 출력
    # 공격 후 남은 플레이어 hp 출력
    player_hp -= monster_damage
    print(f"몬스터 공격! 데미지: {monster_damage} | 플레이어 HP: {player_hp}")
    print()
    
    # 플레이어 hp가 0 이하가 되면 몬스터 승리, break
    if player_hp <= 0:
        p_lose = True
        break

# 유저가 지면 몬스터 승리 출력
print()
if p_lose:
    print("몬스터 승리... (플레이어 패배)")

# 이기면 턴 횟수 출력
else:
    print(f"플레이어 승리! ({turn}턴 만에 승리)")