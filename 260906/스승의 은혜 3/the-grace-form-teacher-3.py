N, B = map(int, input().split())

gifts = [tuple(map(int, input().split())) for _ in range(N)]

P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

answer = 0

for i in range(N):
    costs = []

    for j in range(N):
        if i == j:
            costs.append(P[j] // 2 + S[j])
        else:
            costs.append(P[j] + S[j])

    costs.sort()

    total = 0
    count = 0

    for cost in costs:
        if total + cost <= B:
            total += cost
            count += 1
        else:
            break

    answer = max(answer, count)

print(answer)