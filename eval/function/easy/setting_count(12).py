raw = input().split()
name = ""
settings = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        settings[k] = v
    else:
        name = t

def config(name, **settings):
    """
    이름(name)과 설정(settings)를 받아
    {name} has {len(settings)} settings 문자열을 반환하는 함수

    config("서버", "host"="localhost", "port"="8080")       -> 서버 has 2 settings

    Args: name(str), settings(dict)
    Returns: str
    """
    return f"{name} has {len(settings)} settings"

# ↓ 호출부 (수정하지 마세요)
print(config(name, **settings))
