T, a, b = map(int, input().split())

S = []
N = []

for _ in range(T):
    c, x = input().split()
    x = int(x)

    if c == 'S':
        S.append(x)
    else:
        N.append(x)

answer = 0

for k in range(a, b + 1):
    d1 = min(abs(k - s) for s in S)
    d2 = min(abs(k - n) for n in N)

    if d1 <= d2:
        answer += 1

print(answer)
