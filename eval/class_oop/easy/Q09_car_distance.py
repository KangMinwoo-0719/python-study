class Car:
    """
    차 이름과 남은 연료를 입력받은 후
    주행 거리를 입력받을 때 마다 남은 연료를 계산하는 클래스
    """

    def __init__(self, model, fuel):
        """
        자동차 이름, 연료 속성 생성
        """
        self.model = model
        self.fuel = fuel

    def drive(self, km):
        """
        주행거리를 입력 받아 연료 1 단위로 10km씩 주행거리를 계산하는 메서드
        """
        distance = min(km, self.fuel * 10)
        self.fuel -= distance // 10
        return distance

    def status(self):
        """
        남은 연료를 보여주는 문자열을 반환하는 메서드
        """
        return f"{self.model} 남은 연료 {self.fuel}"

# 첫 줄: "모델명 연료" (예: "소나타 5" -> model="소나타", fuel=5)
# 둘째 줄: 주행 요청 거리들 (예: "20 15 30" -> [20, 15, 30])
model, fuel = input().split()
fuel = int(fuel)
trips = [int(x) for x in input().split()]

# ---- 호출부 (수정 금지) ----
car = Car(model, fuel)
print(car.status())
for km in trips:
    driven = car.drive(km)
    print(f"요청 {km}km -> 주행 {driven}km")
    print(car.status())