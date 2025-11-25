import sys
input = sys.stdin.readline

x = int(input())
dp = [0] * (x + 1)

# DP, 바텀업
for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1   # -1 연산
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)   # /2 연산
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)   # /3 연산

print(dp[x])
