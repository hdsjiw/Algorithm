n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

answer = n

for px in range(0, 101, 2):      # 세로선 x = px
    for py in range(0, 101, 2):  # 가로선 y = py

        cnt = [0, 0, 0, 0]

        for x, y in points:
            if x < px and y < py:
                cnt[0] += 1
            elif x < px and y > py:
                cnt[1] += 1
            elif x > px and y < py:
                cnt[2] += 1
            else:
                cnt[3] += 1

        answer = min(answer, max(cnt))

print(answer)