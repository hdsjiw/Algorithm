from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    table = defaultdict(list)

    # 1. 지원자 정보를 모든 조건 조합에 등록
    for person in info:
        data = person.split()

        conditions = data[:4]
        score = int(data[4])

        # 4개 조건 각각을 실제 값 / "-" 두 가지로 만들기
        for mask in range(16):
            key = []

            for i in range(4):
                if mask & (1 << i):
                    key.append("-")
                else:
                    key.append(conditions[i])

            table[" ".join(key)].append(score)

    # 2. 각 조건별 점수 정렬
    for key in table:
        table[key].sort()

    # 3. query 처리
    answer = []

    for q in query:
        q = q.replace(" and ", " ").split()

        key = " ".join(q[:4])
        target = int(q[4])

        scores = table[key]

        # target 이상이 처음 등장하는 위치
        idx = bisect_left(scores, target)

        answer.append(len(scores) - idx)

    return answer