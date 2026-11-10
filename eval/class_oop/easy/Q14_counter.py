class Counter:
    """
    첫 시작값을 받고 입력받은 호출 방식을 입력받아
    호출받은 개수만큼 카운트 후 카운트 값을 반환하는 클래스
    """
    
    def __init__(self, start: int) -> None:
        """
        카운트 초기 시작값을 받아 인스턴스 속성 변수 count를 만드는 생성자
        """
        # 인스턴스 변수 count 정의
        self.count = start

    def inc(self):
        """
        호출 될 때 마다 인스턴스 변수 count 값을 카운트 후 반환하는 메서드
        """
        # count 값 + 1 후 반환하기
        self.count += 1
        return self.count

    def value(self):
        """
        count 값을 반환하는 메서드
        """
        # count 값 반환하기
        return self.count

# 첫 줄: 시작값 start. 둘째 줄: 호출 방식 목록 (예: "obj cls obj" -> ["obj", "cls", "obj"])
start = int(input())
hows = input().split()

# ---- 호출부 (수정 금지) ----
c = Counter(start)
for how in hows:
    if how == "obj":
        print("c.inc() ->", c.inc())               # 인스턴스로 호출
    else:
        print("Counter.inc(c) ->", Counter.inc(c))  # 클래스로 호출 (객체를 첫 인자로 직접 전달)
print("value:", c.value())
print(c.value() == Counter.value(c))