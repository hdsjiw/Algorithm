n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

x, y = zip(*points)

x, y = list(x), list(y)


def solve(remaining, cnt):
    # 모든 점을 이미 지났으면 성공
    if not remaining:
        return True

    # 직선 3개를 이미 사용했는데 점이 남아있으면 실패
    if cnt == 3:
        return False

    # 아직 지나지 않은 점 하나 선택
    idx = remaining[0]
    px, py = points[idx]

    # 1. 이 점을 지나는 세로선 x = px
    next_remaining = [
        i for i in remaining
        if points[i][0] != px
    ]

    if solve(next_remaining, cnt + 1):
        return True

    # 2. 이 점을 지나는 가로선 y = py
    next_remaining = [
        i for i in remaining
        if points[i][1] != py
    ]

    if solve(next_remaining, cnt + 1):
        return True

    return False


if solve(list(range(n)), 0):
    print(1)
else:
    print(0)