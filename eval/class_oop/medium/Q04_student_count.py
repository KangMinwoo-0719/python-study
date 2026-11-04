# 한 줄에 이름들이 공백으로 구분되어 있습니다. 예: "kim lee" -> ["kim", "lee"]
names = input().split()

class Student:
    count = 0

    def __init__(self, name):
        self.name = name

        # 클래스 속성 변수에 값 누적
        Student.count += 1
        
        # 학번 문자열 저장
        self.uid = f"S{self.count:03d}"

    @classmethod
    def total(cls):

        # 학생 수 누적값 반환
        return cls.count

# ---- 호출부 (수정 금지) ----
students = [Student(name) for name in names]
for s in students:
    print(s.uid, s.name)
print(Student.total())
print(students[0].count == Student.count, "count" in students[0].__dict__)