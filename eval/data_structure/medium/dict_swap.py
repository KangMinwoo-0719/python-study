scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
target = int(input())

# 점수, 이름 순서로 swap하여 새로운 딕셔너리 생성
swap_scores = {score: name for name, score in scores.items()}

# 해당 딕셔너리에서 target 점수 이름 출력
if target in swap_scores.keys():
    print(swap_scores[target])

else:
    print("없음")