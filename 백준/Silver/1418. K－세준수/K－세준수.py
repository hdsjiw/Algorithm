import sys,math

input = sys.stdin.readline

n=int(input())
k=int(input())

max_prime = [0] * (n + 1)

for i in range(2, n + 1):
    if max_prime[i] == 0:  # i가 소수라면
        for j in range(i, n + 1, i):
            max_prime[j] = i  # j의 소인수 중 i 기록 (나중에 최대값이 될 수 있음)

count = 0
for x in range(1, n + 1):
    if max_prime[x] <= k:
        count += 1

print(count)
