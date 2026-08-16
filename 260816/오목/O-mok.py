board = [list(map(int, input().split())) for _ in range(19)]

# 오른쪽, 아래, 오른쪽 아래, 오른쪽 위
dr = [0, 1, 1, -1]
dc = [1, 0, 1, 1]

for r in range(19):
    for c in range(19):

        if board[r][c] == 0:
            continue

        color = board[r][c]

        for d in range(4):
            # 현재 위치가 해당 오목의 시작점인지 확인
            prev_r = r - dr[d]
            prev_c = c - dc[d]

            if 0 <= prev_r < 19 and 0 <= prev_c < 19:
                if board[prev_r][prev_c] == color:
                    continue

            # 같은 색 돌이 정확히 5개인지 확인
            count = 0
            nr, nc = r, c

            while (
                0 <= nr < 19
                and 0 <= nc < 19
                and board[nr][nc] == color
            ):
                count += 1
                nr += dr[d]
                nc += dc[d]

            if count == 5:
                print(color)

                middle_r = r + dr[d] * 2
                middle_c = c + dc[d] * 2

                print(middle_r + 1, middle_c + 1)
                exit()

print(0)
