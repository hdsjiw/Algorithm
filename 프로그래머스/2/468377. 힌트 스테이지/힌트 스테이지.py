
def solution(cost, hint):
    n = len(cost)
    answer = float('inf')

    for mask in range(1 << (n - 1)):
        counts = [0] * n
        total = 0

        # 1. 구매할 힌트 번들 결정
        for i in range(n - 1):
            if mask & (1 << i):
                total += hint[i][0]

                for stage in hint[i][1:]:
                    counts[stage - 1] += 1

        # 2. 각 스테이지 해결 비용 합산
        for i in range(n):
            used = min(counts[i], n - 1)
            total += cost[i][used]

        # 3. 최소 비용 갱신
        answer = min(answer, total)

    return answer
