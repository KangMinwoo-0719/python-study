class Book:
    def __init__(self, title: str, author: str, pages: int):
        """제목, 저자, 쪽수를 받는 생성자"""
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        """
        title, author, pages를 포매팅 한 문자열을 반환한다.
        """
        # "{title} - {author} ({pages}쪽)" 형식의 문자열 반환
        return f"{self.title} - {self.author} ({self.pages}쪽)"

    def is_long(self):
        """
        쪽 수(pages)가 300 이상인 경우 True, 아닌 경우 False를 반환
        """
        # pages boolean 반환
        return self.pages >= 300

# 첫 줄: 도서 수 n. 이어지는 n 줄: "제목 저자 쪽수" (예: "파이썬 김철수 250" -> ["파이썬", "김철수", "250"])
n = int(input())
rows = [input().split() for _ in range(n)]

# ------ 호출부 (수정 금지) ------
for title, author, pages in rows:
    book = Book(title, author, int(pages))
    print(book.describe())
    print(book.is_long())