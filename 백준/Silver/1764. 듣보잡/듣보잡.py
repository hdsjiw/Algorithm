import sys

n, m = map(int, sys.stdin.readline().split())

no_heard = set()
no_see = set()

for _ in range(n):
    no_heard.add(sys.stdin.readline().strip())

for _ in range(m):
    no_see.add(sys.stdin.readline().strip())

# 교집합 구하기
answer = sorted(no_heard & no_see)

print(len(answer))
print("\n".join(answer))
