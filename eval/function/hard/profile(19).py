raw = input().split()
pos = [t for t in raw if "=" not in t]
name = pos[0]
roles = pos[1:]
status = "active"
meta = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "status":
            status = v
        else:
            meta[k] = v

# TODO: 여기에 함수 profile(name, *roles, status="active", **meta) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
def profile(name, *roles, status="activate", **meta):
    """
    이름(name), 임의 개수 역할(roles), 상태(status), 그 외 정보(meta)를 입력받아
    "{name}[{status}] 역할{len(roles)} 정보{len(meta)}" 형식의 문자열을 반환하는 함수
    """

    return f"{name}[{status}] 역할{len(roles)} 정보{len(meta)}"

# ↓ 호출부 (수정하지 마세요)
print(profile(name, *roles, status=status, **meta))