import sys
input = sys.stdin.readline

n = int(input())

MOD = 10**20  # 넉넉히 크게 유지 (뒤 5자리만 출력하지만 중간 정보 보존용)

res = 1
cnt2 = 0
cnt5 = 0

for i in range(2, n + 1):
    x = i
    while x % 2 == 0:
        cnt2 += 1
        x //= 2
    while x % 5 == 0:
        cnt5 += 1
        x //= 5

    res = (res * x) % MOD

# 2가 항상 더 많으므로 남은 2만 곱해줌
res = (res * pow(2, cnt2 - cnt5, MOD)) % MOD

# 마지막 0이 아닌 5자리 (앞자리 0 포함)
print(f"{res % 100000:05d}")
