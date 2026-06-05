money = int(input())
coin_total = 0

# 500 단위 계산 후 저장
coin_500 = money // 500
print(f"500원: {coin_500}개")

# 100 단위 계산 후 저장
coin_100 = (money % 500) // 100
print(f"100원: {coin_100}개")

# 50 단위 계산 후 저장
coin_50 = (money % 100) // 50
print(f"50원: {coin_50}개")

# 10 단위 계산 후 저장 
coin_10 = (money % 100 % 50) // 10
print(f"10원: {coin_10}개")

coin_total = coin_10 + coin_50 + coin_100 + coin_500

# 총 동전개수 출력
print(f"총 동전 수: {coin_total}개")