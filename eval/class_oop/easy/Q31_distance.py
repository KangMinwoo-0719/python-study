class Distance:
    """"""

    @staticmethod
    def km_to_m(km):
        """
        km 단위를 받아 1000을 곱한 값을 반환하는 메서드
        """
        return km * 1000

    @staticmethod
    def m_to_km(m):
        """
        m 단위를 받아 1000을 나눈 값을 반환하는 메서드
        """
        return m / 1000

# 첫 줄: 요청 수 n. 이어지는 n 줄: "K 3" 또는 "M 1500" (kind 는 'K'/'M', value 는 정수)
n = int(input())
requests = []
for _ in range(n):
    kind, value = input().split()
    requests.append((kind, int(value)))

# ---- 호출부 (수정 금지) ----
conv = Distance()
for kind, value in requests:
    if kind == "K":
        print(Distance.km_to_m(value))           # 클래스 이름으로 직접 호출
    else:
        print(f"{conv.m_to_km(value):.3f}")      # 인스턴스로 호출