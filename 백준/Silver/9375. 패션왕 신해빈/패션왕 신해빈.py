import sys

input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n = int(input())
    kinds = {}

    for _ in range(n):
        name, kind = input().split()
        if kind in kinds:
            kinds[kind] += 1
        else:
            kinds[kind] = 1

    result = 1
    for count in kinds.values():
        result *= (count + 1)

    print(result - 1)
    