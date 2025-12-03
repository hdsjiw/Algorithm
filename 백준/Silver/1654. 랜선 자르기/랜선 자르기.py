import sys
input = sys.stdin.readline

k, n = map(int, input().split())
l = [int(input()) for _ in range(k)]

start, end = 1, max(l)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0

    for length in l:
        count += length // mid

    if count >= n:   # 더 크게 잘라도 됨 → 길이를 늘림
        result = mid
        start = mid + 1
    else:            # 너무 크게 잘랐음 → 길이를 줄임
        end = mid - 1

print(result)
