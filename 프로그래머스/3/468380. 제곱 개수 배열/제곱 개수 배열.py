
from bisect import bisect_right

def solution(arr, l, r):
    ends = [0]
    sums = [0]

    for x in arr:
        ends.append(ends[-1] + x)
        sums.append(sums[-1] + x * x)

    total = ends[-1]
    L = r - l + 1

    def prefix(pos):
        i = bisect_right(ends, pos) - 1

        if i == len(arr):
            return sums[-1]

        return sums[i] + (pos - ends[i]) * arr[i]

    K = prefix(r) - prefix(l - 1)
    last = total - L

    points = {0, last + 1}

    for p in ends[1:-1]:
        if 0 < p <= last:
            points.add(p)

        if 0 < p - L <= last:
            points.add(p - L)

    points = sorted(points)
    count = 0

    for a, b in zip(points, points[1:]):
        current = prefix(a + L) - prefix(a)

        # 마지막 시작 위치는 별도로 처리
        if a == last:
            if current == K:
                count += 1
            continue

        left = arr[bisect_right(ends, a) - 1]
        right = arr[bisect_right(ends, a + L) - 1]

        diff = right - left

        if diff == 0:
            if current == K:
                count += b - a
        else:
            gap = K - current

            if gap % diff == 0:
                steps = gap // diff

                if 0 <= steps < b - a:
                    count += 1

    return [K, count]
