n = int(input())

people = [tuple(input().split()) for _ in range(n)]

people.sort(key=lambda x: int(x[0]))

pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

ans = 0

for i in range(n):
    g = 0
    h = 0

    for j in range(i, n):
        if alpha[j] == 'G':
            g += 1
        else:
            h += 1

        if g == 0 or h == 0 or g == h:
            ans = max(ans, pos[j] - pos[i])

print(ans)