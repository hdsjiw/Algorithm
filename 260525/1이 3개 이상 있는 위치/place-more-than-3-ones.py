n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

for x in range(n):
    for y in range(n):
        count = 0

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1:
                    count += 1

        if count >= 3:
            answer += 1

print(answer)
