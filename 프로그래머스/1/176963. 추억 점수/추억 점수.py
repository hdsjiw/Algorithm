def solution(name, yearning, photo):
    score_map = dict(zip(name, yearning))  # 이름 → 점수 매핑
    answer = []

    for people in photo:
        score = 0
        for person in people:
            score += score_map.get(person, 0)  # 없으면 0
        answer.append(score)

    return answer