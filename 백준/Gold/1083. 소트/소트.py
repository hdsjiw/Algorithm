import sys
input = sys.stdin.readline

n=int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n):
    if s == 0:
        break

    # 현재 위치에서 이동 가능한 범위
    max_idx = i
    for j in range(i + 1, min(n, i + s + 1)):
        if arr[j] > arr[max_idx]:
            max_idx = j

    # 가장 큰 값을 앞으로 당김
    for j in range(max_idx, i, -1):
        arr[j], arr[j - 1] = arr[j - 1], arr[j]

    # 사용한 이동 횟수 차감
    s -= (max_idx - i)

print(*arr)
