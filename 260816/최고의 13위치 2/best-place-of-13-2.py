n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

blocks = []

# 가능한 모든 1 x 3 구간
for r in range(n):
    for c in range(n - 2):
        cnt = arr[r][c] + arr[r][c + 1] + arr[r][c + 2]
        blocks.append((r, c, cnt))

answer = 0

for i in range(len(blocks)):
    r1, c1, cnt1 = blocks[i]

    for j in range(i + 1, len(blocks)):
        r2, c2, cnt2 = blocks[j]

        # 서로 다른 행이면 절대 겹치지 않음
        if r1 != r2:
            answer = max(answer, cnt1 + cnt2)

        else:
            # 같은 행이면 구간이 겹치지 않아야 함
            # [c1, c1+2], [c2, c2+2]
            if c1 + 2 < c2 or c2 + 2 < c1:
                answer = max(answer, cnt1 + cnt2)

print(answer)