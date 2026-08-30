n = int(input())

times = [tuple(map(int, input().split())) for _ in range(n)]

a = [t[0] for t in times]
b = [t[1] for t in times]

ans = 0

for fire in range(n):
    working = [0] * 1001

    for i in range(n):
        if i == fire:
            continue

        for t in range(a[i], b[i]):
            working[t] = 1

    total = sum(working)
    ans = max(ans, total)

print(ans)