from collections import Counter

def solution(weights):
    count = Counter(weights)
    answer = 0

    for w in count:
        n = count[w]

        # 1. 같은 몸무게끼리
        answer += n * (n - 1) // 2

        # 2. 서로 다른 몸무게
        for a, b in [(2, 3), (2, 4), (3, 4)]:
            if w * b % a == 0:
                other = w * b // a

                if other in count:
                    answer += n * count[other]

    return answer