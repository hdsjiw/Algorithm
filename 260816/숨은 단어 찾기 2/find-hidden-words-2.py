N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# 8방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

answer = 0

for i in range(N):
    for j in range(M):

        if arr[i][j] != 'L':
            continue

        for d in range(8):
            x1 = i + dx[d]
            y1 = j + dy[d]

            x2 = i + dx[d] * 2
            y2 = j + dy[d] * 2

            if (
                0 <= x1 < N and 0 <= y1 < M
                and 0 <= x2 < N and 0 <= y2 < M
            ):
                if arr[x1][y1] == 'E' and arr[x2][y2] == 'E':
                    answer += 1

print(answer)