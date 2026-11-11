class Box:
    """
    박스의 개수, 세 변의 길이를 받아 
    각 박스의 겉넓이와 부피를 계산하는 클래스
    """

    def __init__(self, w: int, h: int, d: int) -> None:
        """인스턴스 속성 변수 w, h, d를 정의하는 생성자"""
        self.w = w
        self.h = h
        self.d = d

    def volume(self) -> int:
        """각 세 변의 길이를 계산하여 부피를 반환하는 메서드"""
        # 부피 = 세 개의 변을 모두 곱한 값을 반환
        return self.w * self.h * self.d
        

    def surface(self) -> int:
        """상자의 겉넓이를 계산하여 반환하는 메서드"""
        # 각 세 개의 면적을 구한 후 2를 곱하여 전체 면적의 겉넓이 계산
        return 2 * (self.h * self.d + self.h * self.w + self.d * self.w)

    def describe(self) -> str:
        """세 변의 길이와 부피, 겉넓이의 값을 문자열로 묶어 반환하는 메서드"""
        # "{w}x{h}x{d}: 부피{volume}, 겉넓이{surface}" 형식의 문자열로 반환
        return f"{self.w}x{self.h}x{self.d}: 부피 {self.volume()}, 겉넓이 {self.surface()}"
        
# 첫 줄: 상자 수 n. 이어지는 n 줄: "가로 세로 높이" (예: "2 3 4" -> [2, 3, 4])
n = int(input())
rows = [list(map(int, input().split())) for _ in range(n)]

# ---- 호출부 (수정 금지) ----
for w, h, d in rows:
    box = Box(w, h, d)
    print(box.volume())
    print(box.surface())
    print(box.describe())