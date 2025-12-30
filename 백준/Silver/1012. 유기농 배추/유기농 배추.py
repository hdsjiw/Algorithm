import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(t):
    m, n, k = map(int, input().split())  # m: 가로, n: 세로
    field = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1   # y가 행, x가 열

    def bfs(sx, sy):
        q = deque()
        q.append((sx, sy))
        field[sx][sy] = 0

        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
                    field[nx][ny] = 0
                    q.append((nx, ny))

    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)
