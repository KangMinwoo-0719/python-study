class Dog:
    """
    이름과 나이를 입력받아 사람 나이로 환산해 주는 클래스
    """

    def __init__(self, name: str, age: int):
        """
        인스턴스 속성 name, age를 정의하는 생성자
        """

        self.name = name
        self.age = age

    def bark(self):
        """
        "{name}: 멍멍" 문자열을 반환하는 함수
        """

        # self.name + "멍멍" 문자열을 반환
        return f"{self.name}: 멍멍"
 
    def human_age(self):
        """
        입력받은 나이(age)를 사람 나이로 환산 후 반환하는 함수
        """
        # self.age * 7 값을 반환하기
        return self.age * 7

# 첫 줄: 강아지 수 n. 이어지는 n 줄: "이름 나이" (예: "바둑이 3" -> ["바둑이", "3"])
n = int(input())
rows = [input().split() for _ in range(n)]


# ---- 호출부 (수정 금지) ----
for dog_name, dog_age in rows:
    dog = Dog(dog_name, int(dog_age))
    print(dog.bark())
    print(f"{dog.name} {dog.age}살 = 사람 나이 {dog.human_age()}살")