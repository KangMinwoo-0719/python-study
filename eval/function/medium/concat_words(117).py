words = input().split()

def concat_words(*words):
    """
    단어 리스트(words)를 받아
    단어 사이에 구분자("-")를 넣어 연결한 문자열을 반환하는 함수
    """

    return "-".join(words)

# ↓ 호출부 (수정하지 마세요)
print(concat_words(*words))