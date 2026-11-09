class Clock:
    """
    첫 시각(h, m)을 입력받고 이후 추가로 받는 분(m)을 더한
    시각을 반환하는 클래스
    """

    def __init__(self, h, m):
        """
        입력받은 시간(h), 분(m)을 인스턴스 속성으로 저장하는 생성자
        """
        self.h = h
        self.m = m

    def tick(self, minutes):
        """
        입력받은 시각 + minutes 값을 계산하는 메서드
        """
        # 분(m) + minutes 연산 후 60분 이상인 경우 - 60 후 h + m // 60
        self.m += minutes
        self.h += self.m // 60
        self.m %= 60

        # 24시 이상일 시 미만이 될 때 까지 빼기
        self.h %= 24

        # 시간(h)가 24 이상인 경우 h - 24

    def show(self):
        """
        반환한 시간을 "HH:MM" 형식의 문자열로 반환하는 메서드
        """
        str_h = ""
        str_m = ""
        # 시간(h), 분(m)의 길이가 2 미만인 경우 각각 앞자리에 "0" 추가하기
        str_h = "0" + str(self.h) if len(str(self.h)) < 2 else str(self.h)
        str_m = "0" + str(self.m) if len(str(self.m)) < 2 else str(self.m)

        # 계산된 값을 "HH:MM" 형식으로 반환하기
        return f"{str_h}:{str_m}"

# 첫 줄: "시 분" (예: "9 30" -> h=9, m=30)
# 둘째 줄: 진행시킬 분들 (예: "15 45" -> [15, 45])
h, m = [int(x) for x in input().split()]
ticks = [int(x) for x in input().split()]

# ---- 호출부 (수정 금지) ----
clock = Clock(h, m)
print(clock.show())
for minutes in ticks:
    clock.tick(minutes)
    print(f"+{minutes}분 -> {clock.show()}")