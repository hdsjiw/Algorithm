n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

x = [p[0] for p in points]
y = [p[1] for p in points]

ans = float('inf')

for i in range(n):
    remain_x = []
    remain_y = []

    for j in range(n):
        if i == j:
            continue

        remain_x.append(x[j])
        remain_y.append(y[j])

    width = max(remain_x) - min(remain_x)
    height = max(remain_y) - min(remain_y)

    area = width * height
    ans = min(ans, area)

print(ans)
