"""
TITLE: 합격 판별기
DIFFICULTY: easy
TAGS: if, comparison, print
EVAL: stdio

DESCRIPTION:
점수를 입력받아 80점 이상이면 `합격`을 출력하시오.
80점 미만이면 아무것도 출력하지 마시오.

예시:
- 입력: `85` → 출력: `합격`
- 입력: `70` → 출력: (없음)
- 입력: `80` → 출력: `합격`
"""

# 점수를 입력받아 80점 이상이면 "합격"을 출력하세요.
score = int(input())

# 입력받은 score가 80점 이상일 경우에만 "합격" 출력
if score >= 80:
    print("합격")