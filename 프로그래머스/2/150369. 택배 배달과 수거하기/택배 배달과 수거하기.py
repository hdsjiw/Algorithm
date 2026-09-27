def solution(cap, n, deliveries, pickups):
    answer = 0
    d = n - 1  # 배달이 남은 가장 먼 집
    p = n - 1  # 수거가 남은 가장 먼 집

    while True:
        while d >= 0 and deliveries[d] == 0:
            d -= 1
        while p >= 0 and pickups[p] == 0:
            p -= 1

        if d < 0 and p < 0:
            break

        # 이번에 가야 하는 가장 먼 집까지 왕복
        answer += 2 * (max(d, p) + 1)

        remaining = cap
        while d >= 0 and remaining > 0:
            taken = min(deliveries[d], remaining)
            deliveries[d] -= taken
            remaining -= taken
            if deliveries[d] == 0:
                d -= 1

        remaining = cap
        while p >= 0 and remaining > 0:
            taken = min(pickups[p], remaining)
            pickups[p] -= taken
            remaining -= taken
            if pickups[p] == 0:
                p -= 1

    return answer