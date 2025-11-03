import sys

t=int(sys.stdin.readline())

# 미리 0~40까지의 0과 1 호출 횟수를 DP로 계산
dp = [(1, 0), (0, 1)]  # (0 호출 수, 1 호출 수)
for i in range(2, 41):
    a0, a1 = dp[i-1]
    b0, b1 = dp[i-2]
    dp.append((a0 + b0, a1 + b1))

for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n][0], dp[n][1])
    