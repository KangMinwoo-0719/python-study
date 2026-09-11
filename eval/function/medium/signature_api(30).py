raw = input().split()
pos = [t for t in raw if "=" not in t]
endpoint = pos[0]
args = pos[1:]
method = "GET"
headers = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "method":
            method = v
        else:
            headers[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def api(endpoint, *args, method="GET", **other):
    return endpoint + " " + method + " a" + str(len(args)) + " h" + str(len(other))


# 함수 호출 후 각 인자값을 입력 후 반환값 출력
print(api(endpoint, *args, method=method, **headers))