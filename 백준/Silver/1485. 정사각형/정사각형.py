import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    points = [tuple(map(int, input().split())) for _ in range(4)]
    dist = []

    for i in range(4):
        for j in range(i + 1, 4):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist.append(dx*dx + dy*dy)

    dist.sort()

    # 정사각형 조건
    if (
        dist[0] > 0 and
        dist[0] == dist[1] == dist[2] == dist[3] and
        dist[4] == dist[5] and
        dist[4] == dist[0] * 2
    ):
        print(1)
    else:
        print(0)
