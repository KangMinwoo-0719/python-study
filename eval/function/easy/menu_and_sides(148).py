raw = input().split()
name = raw[0]
sides = raw[1:]

# TODO: 여기에 함수 menu(name, *sides) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def menu(name, *sides):
    """
    주 메뉴(menu), 반찬(sides)를 입력받아
    menu (sides) 형식을 반환하는 함수

    menu("비빔밥", ("김치", "단무지")) 
    """
    
    if sides:
        return f"{name} ({','.join(sides)})"
    else:
        return f"{name}"
    

# ↓ 호출부 (수정하지 마세요)
print(menu(name, *sides))