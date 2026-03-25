# 모듈 읽어들이기
from urllib import request

# urlopen 함수로 구글 메인페이지 읽기
target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")


output = target.read()
print(output)   

# wb = Write Binary(바이너리 쓰기 모드)
file = open("output.png", "wb")
file.write(output)
file.close()