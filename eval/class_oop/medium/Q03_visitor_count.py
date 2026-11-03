class Visitor:
    """
    방문자 명단과 인원을 받는 유틸리티 클래스
    """
    total = 0

    def __init__(self, name):
        """
        인원 이름을 받아 카운트 하는 클래스메서드
        """
        self.name = name
        Visitor.total += 1
        self.number = Visitor.total

    @classmethod
    def get_total(cls):
        """
        총 누적 합 인원을 반환하는 함수
        """
        return cls.total

    def greet(self):
        """
        방문자 이름과 순서 문자열을 반환하는 함수
        """
        return f"{self.name}님, {self.number}번째 방문자입니다"

# 한 줄에 이름들이 공백으로 구분되어 있습니다. 예: "kim lee park" -> ["kim", "lee", "park"]
names = input().split()

# ---- 호출부 (수정 금지) ----
visitors = [Visitor(name) for name in names]
for v in visitors:
    print(v.greet())
print(Visitor.get_total())
print(Visitor.total == len(visitors), "total" in visitors[0].__dict__)
