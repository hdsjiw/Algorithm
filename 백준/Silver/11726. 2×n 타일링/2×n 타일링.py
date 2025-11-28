import sys
input = sys.stdin.readline

n = int(input())

# 예외 처리
if n == 1:
    print(1)
    exit()

dp = [0] * n
dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n-1])
