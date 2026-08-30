n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

x = [p[0] for p in points]
y = [p[1] for p in points]

ans = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            # i, j가 x축과 평행한 변
            if y[i] == y[j]:
                # i, k가 y축과 평행한 변
                if x[i] == x[k]:
                    width = abs(x[i] - x[j])
                    height = abs(y[i] - y[k])

                    ans = max(ans, width * height)

print(ans)
