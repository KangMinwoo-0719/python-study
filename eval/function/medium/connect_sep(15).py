raw = input().split()
pos = [t for t in raw if "=" not in t]
first = pos[0]
rest = pos[1:]
sep = "-"
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "sep":
            sep = v

def make_list(first, *rest, sep="-"):
    """
    첫 항목(first)과 나머지 항목(rest), 구분자(sep)을 입력받아
    항목 사이에 구분자를 넣은 문자열을 반환하는 함수
    """
    # 항목들을 list 형으로 변환한 뒤 구분자를 넣어 합하여 반환
    return sep.join([first] + list(rest))

print(make_list(first, *rest, sep=sep))