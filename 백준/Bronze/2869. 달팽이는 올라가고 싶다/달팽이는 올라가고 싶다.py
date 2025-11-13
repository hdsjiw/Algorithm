a, b, v = map(int, input().split())

# 마지막 날은 미끄러지지 않으니까,
# (v - b)를 하루에 실제로 오르는 거리 (a - b)로 나누면 된다.
day = (v - b - 1) // (a - b) + 1

print(day)