class Animal:
    """
    동물의 종류를 받아 이름과 다리 개수, 인스턴스 속성에 포함되어 있는지 확인하는 클래스
    """
    legs = 4

    def __init__(self, name):
        """인스턴스 속성 name 정의하는 생성자"""
        self.name = name
    

# 한 줄에 이름들이 공백으로 구분되어 있습니다. 예: "dog cat" -> ["dog", "cat"]
names = input().split()


# ---- 호출부 (수정 금지) ----
animals = [Animal(name) for name in names]
for a in animals:
    print(a.name, a.legs)                                   # 둘 다 읽을 수는 있지만
    print('"name" in a.__dict__:', "name" in a.__dict__)     # name 은 인스턴스에 산다
    print('"legs" in a.__dict__:', "legs" in a.__dict__)     # legs 는 인스턴스에 없다
print('"legs" in Animal.__dict__:', "legs" in Animal.__dict__)
print('"name" in Animal.__dict__:', "name" in Animal.__dict__)
print(animals[0].legs == animals[1].legs == Animal.legs)