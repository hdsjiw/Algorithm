n = int(input())
a = [int(input()) for _ in range(n)]

total_people = sum(a)

# 1번 방에서 시작할 때 거리 합
current_dist = 0

for i in range(n):
    current_dist += a[i] * i

min_dist = current_dist

# 시작 방을 1번 → 2번 → ... → N번으로 이동
for i in range(n - 1):
    current_dist = current_dist - total_people + n * a[i]
    min_dist = min(min_dist, current_dist)

print(min_dist)