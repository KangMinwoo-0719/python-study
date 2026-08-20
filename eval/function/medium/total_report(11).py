raw = input().split()
pos = [t for t in raw if "=" not in t]
title = pos[0]
values = [int(x) for x in pos[1:]]
unit = "개"
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "unit":
            unit = v

# TODO: 여기에 함수 report(title, *values, unit="개") 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def report(title, *values, unit="개"):
    """
    제목(title), 개수(values), 단위 문자열(unit)을 받아
    {title}: {sum(values)}{unit} 형식의 문자열을 반환하는 함수
    """

    return f"{title}: {sum(values)}{unit}"

# ↓ 호출부 (수정하지 마세요) — unit 은 키워드 전용이라 이름으로 전달
print(report(title, *values, unit=unit))