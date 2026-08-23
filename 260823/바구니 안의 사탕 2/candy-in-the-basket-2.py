N, K = map(int, input().split())

candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

arr = [0] * 101

for i in range(N):
    arr[pos[i]] += candy[i]

ans = 0

for c in range(101):
    total = 0

    for x in range(max(0, c - K), min(100, c + K) + 1):
        total += arr[x]

    ans = max(ans, total)

print(ans)