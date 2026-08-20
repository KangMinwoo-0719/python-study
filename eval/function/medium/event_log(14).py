raw = input().split()
pos = [t for t in raw if "=" not in t]
event = pos[0]
details = pos[1:]
level = "INFO"
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "level":
            level = v

def log_event(event, *details, level="INFO"):
    """
    이벤트 이름(event), 상세 정보(details), 로그 레벨(level)을 받아
    {level}: {event} ({len(details)}) 형식의 문자열을 반환하는 함수
    """

    return f"{level}: {event} ({len(details)})"

# ↓ 호출부 (수정하지 마세요) — level 은 키워드 전용이라 이름으로 전달
print(log_event(event, *details, level=level))